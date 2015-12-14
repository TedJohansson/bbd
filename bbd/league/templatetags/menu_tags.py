from django import template
from league.models import leagues

register = template.Library()

@register.inclusion_tag('leagues.html')
def getLeagues():
	return {'leagues' : leagues.objects.all()}
