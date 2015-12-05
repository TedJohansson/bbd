from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    full_name = models.CharField(max_length=200, default="Anon")
    favorite_movie = models.CharField(max_length=200, default="The one with the guy.")

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
