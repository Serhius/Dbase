from django.conf.urls import patterns, include, url

urlpatterns = [
	url(r'^login/', 'loginsys.views.login'),
	url(r'^logout/', 'loginsys.views.logout'),
]