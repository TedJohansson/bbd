from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db import connection
from .forms import createLeagueForm
from . import models

def createLeagueView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = createLeagueForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            cursor = connection.cursor()

            u = request.user.id

            cursor.execute("insert into league (leader, name) values (%s, %s)", [u, request.POST.get("league_name", "")])

            cursor.execute("select id from league where leader = %s and name = %s", [u, request.POST.get("league_name", "")])

            league_id = cursor.fetchone() 

            cursor.execute("insert into league_players (league_id, player_id) values (%s, %s)", [league_id, u])

            cursor.execute("select id from auth_user where lower(username) = lower(%s)",[request.POST.get("player1","")])

            player_id = cursor.fetchone()
            
            cursor.execute("insert into league_players (player_id, league_id) values (%s, %s)", [player_id, league_id])


            return HttpResponseRedirect('/league/create/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = createLeagueForm()

    return render(request, 'index/league/create.html', {'form': form})

def leagueMenuView(request):
	query_results = models.leagues.objects.raw("select * from league_leagues")

	league_data = {
		"league_details" : query_results
	}
	print league_data
	return render_to_response('header.html', league_data, context_instance=RequestContext(request))