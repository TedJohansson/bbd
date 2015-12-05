from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^profile/$', 'profile_page.views.user_profile'),
)