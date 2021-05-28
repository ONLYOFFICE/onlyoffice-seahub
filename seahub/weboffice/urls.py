# Copyright (c) 2012-2016 Seafile Ltd.
from django.conf.urls import url

from .views import WebofficeFileInfoView, WebofficeFileSaveView

urlpatterns = [
    # RESTful API



# [28/May/2021 01:45:26] "GET /weboffice-api/v1/3rd/onnotify?&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id HTTP/1.0" 404 8346
# [28/May/2021 01:45:26] "GET /weboffice-api/v1/3rd/onnotify?&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id HTTP/1.0" 404 8346
# [28/May/2021 01:45:26] "GET /weboffice-api/v1/3rd/file/online?&_w_third_file_id=lian-file-id&_w_third_appid=AK20210527IUUZGX HTTP/1.0" 404 8346


# [28/May/2021 01:47:16] "GET /weboffice-api/v1/3rd/file/online?&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id HTTP/1.0" 404 8346
# [28/May/2021 01:47:16] "GET /weboffice-api/v1/3rd/file/save?&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id HTTP/1.0" 404 8346
# [28/May/2021 01:47:16] "GET /weboffice-api/v1/3rd/onnotify?&_w_third_appid=AK20210527IUUZGX&_w_third_file_id=lian-file-id HTTP/1.0" 404 8346


    url(r'^file_info/$', WebofficeFileInfoView.as_view(), name='WebofficeFileInfoView'),
    url(r'^file_save/$', WebofficeFileSaveView.as_view(), name='WebofficeFileSaveView'),
]
