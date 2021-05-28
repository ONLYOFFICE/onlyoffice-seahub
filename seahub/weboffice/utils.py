import json
import time
import logging
import requests
import hashlib
from pprint import pprint

from seahub.settings import WPS_WEBOFFICE_APP_ID, WPS_WEBOFFICE_APP_KEY, \
        WPS_WEBOFFICE_GET_APP_TOKEN_URI, WPS_WEBOFFICE_GET_EDIT_URI, \
        WPS_WEBOFFICE_OPENAPI_HOST

logger = logging.getLogger(__name__)


def send_request(method, uri, body=None, cookie=None, headers=None):

    def _sig(content_md5, url, date):

        sha1 = hashlib.sha1(WPS_WEBOFFICE_APP_KEY.lower().encode('utf-8'))
        sha1.update(content_md5.encode('utf-8'))
        sha1.update(url.encode('utf-8'))
        sha1.update("application/json".encode('utf-8'))
        sha1.update(date.encode('utf-8'))

        return "WPS-3:%s:%s" % (WPS_WEBOFFICE_APP_ID, sha1.hexdigest())

    if method == "PUT" or method == "POST" or method == "DELETE":
        body = json.dumps(body)
        content_md5 = hashlib.md5(body.encode('utf-8')).hexdigest()
    else:
        content_md5 = hashlib.md5("".encode('utf-8')).hexdigest()

    date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    header = {"Content-type": "application/json"}
    header['X-Auth'] = _sig(content_md5, uri, date)
    header['Date'] = date
    header['Content-Md5'] = content_md5

    if headers is not None:
        for key, value in headers.items():
            header[key] = value

    url = "{}{}".format(WPS_WEBOFFICE_OPENAPI_HOST, uri)

    resp = requests.request(method, url, data=body, headers=header,
                            cookies=cookie, verify=False)

    return resp


def get_app_token(app_id, scope):

    method = 'GET'
    uri = '{}?app_id={}&scope={}'.format(WPS_WEBOFFICE_GET_APP_TOKEN_URI,
                                         app_id,
                                         scope)

    resp = send_request(method, uri)

    # {'result': 0,
    #  'token': {'app_token': '900ae97d3ae1b5c29eddf62189690549',
    #            'expires_in': 86400}}

    try:
        return json.loads(resp.text)['token']['app_token']
    except KeyError as e:
        logger.error(e)
        logger.error(uri)
        logger.error(resp.status_code)
        logger.error(resp.text)
        print(e)
        print("uri: {}".format(uri))
        print("status: {}".format(resp.status_code))
        print("response data:")
        pprint(json.loads(resp.text))
        return ''


def get_edit_url(can_edit, file_id, file_ext):

    if can_edit:
        scope = 'file_preview,file_edit'
    else:
        scope = 'file_preview'

    file_type = ''
    if file_ext in ('doc', 'dot', 'wps', 'wpt', 'docx', 'dotx', 'docm', 'dotm', 'rtf'):
        file_type = 'w'
    elif file_ext in ('xls', 'xlt', 'et', 'xlsx', 'xltx', 'csv', 'xlsm', 'xltm'):
        file_type = 's'
    elif file_ext in ('ppt', 'pptx', 'pptm', 'ppsx', 'ppsm', 'pps', 'potx', 'potm', 'dpt', 'dps'):
        file_type = 'p'

    app_token = get_app_token(WPS_WEBOFFICE_APP_ID, scope)
    method = 'GET'
    uri = '{}?app_token={}&file_id={}&type={}'.format(WPS_WEBOFFICE_GET_EDIT_URI,
                                                      app_token,
                                                      file_id,
                                                      file_type)

    resp = send_request(method, uri)

    # {'result': 0,
    #  'url': #  'http://39.97.117.71/weboffice/office/w/5c0f55a9115e5e09fc62b738aed88eb4?...'}

    try:
        return json.loads(resp.text)['url']
    except KeyError as e:
        logger.error(e)
        logger.error(uri)
        logger.error(resp.status_code)
        logger.error(resp.text)
        print(e)
        print("uri: {}".format(uri))
        print("status: {}".format(resp.status_code))
        print("response data:")
        pprint(json.loads(resp.text))
        return ''
