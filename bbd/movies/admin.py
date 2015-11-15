from django.contrib import admin

# Register your models here.
from .models import info

class infoAdmin(admin.ModelAdmin):
	list_display = ["__str__", "released"]
	class Meta:
		model = info

admin.site.register(info, infoAdmin)