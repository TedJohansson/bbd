from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField( max_length=200
                                , default="anon")
    favorite_movie = models.CharField( max_length=200
                                     , default="That movie with that guy")

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])