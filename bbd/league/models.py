from django.db import models

# Create your models here.
class leagues(models.Model):
	name = models.CharField(max_length=255)
	leader = models.IntegerField()


	def __unicode__(self):
		return self.name