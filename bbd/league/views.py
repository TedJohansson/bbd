from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required


@login_required
def createLeagueView(request):
	next = request.GET.get('next', '/home/')
 	return render(request, "index/league/create.html", {'redirect_to': next})