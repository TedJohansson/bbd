from django import forms


class createLeagueForm(forms.Form):
	league_name = forms.CharField(label='Name of league', max_length=255)
	player1 = forms.CharField(label='Player 1', max_length=50)
	# player2 = forms.CharField(label='Player 2', max_length=50)
	# player3 = forms.CharField(label='Player 3', max_length=50)
	# player4 = forms.CharField(label='Player 4', max_length=50)
	# player5 = forms.CharField(label='Player 5', max_length=50)
	# player6 = forms.CharField(label='Player 6', max_length=50)
	# player7 = forms.CharField(label='Player 7', max_length=50)
	# player8 = forms.CharField(label='Player 8', max_length=50)
	# player9 = forms.CharField(label='Player 9', max_length=50)