from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
import movies
from . import views

urlpatterns = [
	url(r'^login/$', views.Login),
	url(r'^logout/$', views.Logout),
	url(r'^home/$', views.Home),
	url(r'^movies/$', views.movieview),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)