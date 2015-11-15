from django.shortcuts import render

from .forms import loginDetailsForm
# Create your views here.
def home(request):
	title = 'Welcome'
	if request.user.is_authenticated():
		title = "BBD %s" %(request.user)

	#adding form
	form = loginDetailsForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		#instance.save()
		print instance.email
		context = {
			"title": "Thank you"
		}
	
	return render(request, "home.html", context)