from django.contrib import admin

# Register your models here.
from .forms import loginDetailsForm
from .models import loginDetails

class usersAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	form = loginDetailsForm

admin.site.register(loginDetails,usersAdmin)