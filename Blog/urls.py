from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^basicview/', include('article.urls')),
	url(r'^auth/', include('loginsys.urls')),
	url(r'^dbase/', include('DBase.urls')),
	url(r'^', include('article.urls')),
]
