from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^create/$', 'league.views.createLeagueView'),
)