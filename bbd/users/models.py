from django.db import models

# Create your models here.
class loginDetails(models.Model):
	username = models.CharField(max_length=60)
	password = models.CharField(max_length=60)
	email = models.CharField(max_length=60)
	firstname = models.CharField(max_length=60)
	lastname = models.CharField(max_length=60)

	def __str__(self):
		return self.username