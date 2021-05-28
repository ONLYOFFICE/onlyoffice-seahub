# Copyright (c) 2012-2016 Seafile Ltd.
# encoding: utf-8

import os
import json
import time
import logging
import urllib.request
import urllib.error
import urllib.parse
import requests
import hashlib
import posixpath
import datetime

from rest_framework.views import APIView

from django.http import HttpResponse
from django.core.cache import cache

from pysearpc import SearpcError
from seaserv import seafile_api

from seahub.base.accounts import User, ANONYMOUS_EMAIL
from seahub.base.templatetags.seahub_tags import email2nickname
from seahub.utils import gen_inner_file_get_url, gen_inner_file_upload_url, \
        is_pro_version
from seahub.utils.file_op import ONLINE_OFFICE_LOCK_OWNER, \
        if_locked_by_online_office
from seahub.settings import SITE_ROOT

from seahub.wopi.utils import get_file_info_by_token

logger = logging.getLogger(__name__)
json_content_type = 'application/json; charset=utf-8'

WOPI_LOCK_EXPIRATION = 30 * 60


class WebofficeFileInfoView(APIView):

    def get(self, request):
        """ Weboffice endpoint for get file info
        """

        app_id = request.GET.get('_w_third_appid', '')
        file_id = request.GET.get('_w_third_file_id', '')


        username = 'lian@lian.com'
        repo_id = 'cdd23594-9371-4d12-9211-7bb1235aa9b1' 
        file_path = '/lian-test-weboffice.xlsx'
        file_name = os.path.basename(file_path)

        file_id = seafile_api.get_file_id_by_path(repo_id, file_path)
        download_token = seafile_api.get_fileserver_access_token(repo_id, file_id, 'download', username, use_onetime=True)

        from seahub.utils import gen_file_get_url
        download_url = gen_file_get_url(download_token, file_name)

        repo = seafile_api.get_repo(repo_id)
        file_size = seafile_api.get_file_size(repo.store_id, repo.version, file_id)



        # 返回响应信息提示:
        # a. 其中user_acl 和 watermark 为非必须返回参数，user_acl 用于控制用户权限，不返回则为系统默认值，watermark 只用于预览时添加第三方水印.
        # b. 返回的参数类型必须与示例一致,切莫将int 与string 类型混淆.
        # c. 返回的参数不能为nil,NULL 等,时间戳长度需与示例一致.
        # d. size 必须和文件真实大小保持一致.
        # e. 文件名一定要带格式后缀.
        # g. 文件id 与接入方式前端访问url 的<:fileid>保持一致.

        result = {
            "file": {
                "id": file_id, # 文件id,字符串长度小于32
                "name": file_name, # 文件名(必须带文件后缀)
                "version": 1, # 当前版本号，位数小于11
                "size": file_size, # 文件大小，单位为B(文件真实大小，否则会出现异常)
                "creator": username, # 创建者id，字符串长度小于32
                "create_time": 1136185445, # 创建时间，时间戳，单位为秒
                "modifier": username, # 修改者id，字符串长度小于32
                "modify_time": 1551409818, # 修改时间，时间戳，单位为秒
                "download_url": download_url, # 载地址
                "preview_pages": 3, # 限制预览页数
                "user_acl": {
                    "rename": 1, # 重命名权限，1 为打开该权限，0 为关闭该权限，默认为0
                    "history": 1, # 历史版本权限，1 为打开该权限，0 为关闭该权限,默认为1
                    "copy": 1, # 复制
                    "export": 1, # 导出PDF
                    "print": 1 # 打印
                },
                "watermark": {
                    "type": 1, # 水印类型， 0 为无水印； 1 为文字水印
                    "value": "禁止传阅", # 文字水印的文字，当type 为1 时此字段必选
                    "fillstyle": "rgba( 192, 192, 192, 0.6 )", # 水印的透明度，非必选，有默认值
                    "font": "bold 20px Serif", # 水印的字体，非必选，有默认值
                    "rotate": -0.7853982, # 水印的旋转度，非必选，有默认值
                    "horizontal": 50, # 水印水平间距，非必选，有默认值
                    "vertical": 100 # 水印垂直间距，非必选，有默认值
                }
            },
            "user": {
                "id": "lian@lian.com", # 用户id，长度小于32
                "name": "lian-test-weboffice", # 用户名称
                "permission": "write", # 用户操作权限，write：可编辑，read：预览
                "avatar_url": "https://demo.seafile.top/image-view/avatars/0/1/a72299021077701e7c522c46fdaa87/resized/72/2f43ff588a4910b1c16eab11dd9440b6.png" # 用户头像地址
            }
        }

        from pprint import pprint
        pprint(request.META)
        # 'HTTP_X_WEBOFFICE_FILE_ID': 'lian-file-id',
        # 'HTTP_X_WEBOFFICE_REFERER': 'http://39.97.117.71/weboffice/office/s/5c0f55a9115e5e09fc62b738aed88eb4?_w_appid=AK202105
        # 6AGBVIK&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id',
        # 'HTTP_X_WEBOFFICE_TOKEN': '',
        # 'HTTP_X_WEBOFFICE_USERAGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X '
        #                               '10_14_6) AppleWebKit/537.36 (KHTML, like '
        #                               'Gecko) Chrome/90.0.4430.212 Safari/537.36',
        # 'HTTP_X_WPS_WEBOFFICE_TOKEN': '',
        pprint(result)
        return HttpResponse(json.dumps(result), status=200,
                            content_type=json_content_type)



class WebofficeFileSaveView(APIView):

    def post(self, request):
        """ Weboffice endpoint for save file content
        """

        from pprint import pprint
        pprint(request.data)

        username = 'lian@lian.com'
        repo_id = 'cdd23594-9371-4d12-9211-7bb1235aa9b1' 
        file_path = '/lian-test-weboffice.xlsx'
        file_name = os.path.basename(file_path)

        file_id = seafile_api.get_file_id_by_path(repo_id, file_path)

        try:
            file_obj = request.data.get('file')

            # get file update url
            fake_obj_id = {'online_office_update': True}
            token = seafile_api.get_fileserver_access_token(repo_id,
                                                            json.dumps(fake_obj_id),
                                                            'update',
                                                            username)

            if not token:
                return HttpResponse(json.dumps({}), status=500,
                                    content_type=json_content_type)

            update_url = gen_inner_file_upload_url('update-api', token)

            # update file
            files = {
                'file': file_obj,
                'file_name': os.path.basename(file_path),
                'target_file': file_path,
            }
            requests.post(update_url, files=files)
        except Exception as e:
            logger.error(e)
            return HttpResponse(json.dumps({}), status=500,
                                content_type=json_content_type)

        result = {
            "file": {
                "id": "f132aa30a87064", # 文件id，字符串长度小于32
                "name": "example.doc", # 文件名
                "version": 2, # 当前版本号，位数小于11
                "size": 200, # 文件大小，单位是B
                "download_url": "http://www.xxx.cn/v1/file?fid=f132aa30a87064" # 文件下载地址
            }
        }
        return HttpResponse(json.dumps(result), status=200,
                            content_type=json_content_type)
