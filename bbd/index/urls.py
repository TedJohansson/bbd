from django.conf.urls.static import static
from django.conf.urls import include, patterns, url
from django.conf import settings
import movies
from . import views

urlpatterns = [
	url(r'^accounts/login/$', views.Login),
	url(r'^accounts/logout/$', views.Logout),
	url(r'^home/$', views.Home),
	url(r'^movies/$', views.movieview),
	url(r'^accounts/', include('profile_page.urls')),
	url(r'^league/', include('league.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)