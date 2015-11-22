from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from bbd import settings
from movies import models
from django.contrib.auth.decorators import login_required

def Login(request):
	next = request.GET.get('next', '/home/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user.")
		else:
			HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "index/login.html", {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
	return render(request, "index/home.html", {})

def movieview(request):
	query_results = models.info.objects.raw("select * from movies_info where lower(title) != 'none'")

	movies_data = {
		"movie_details" : query_results
	}
	print movies_data
	return render_to_response('index/movies.html', movies_data, context_instance=RequestContext(request))