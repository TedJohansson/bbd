from django import forms

from .models import loginDetails

class loginDetailsForm(forms.ModelForm):
	class Meta:
		model = loginDetails
		fields = ['username', 'password','email', 'firstname', 'lastname']