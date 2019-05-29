from django.urls import path, re_path
from django.conf.urls import url, include
from .views import dataList, dataDetail

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', dataList.as_view()),
    url(r'^(?P<pk>\d+)', dataDetail.as_view()),
]