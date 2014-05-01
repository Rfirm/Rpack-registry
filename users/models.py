from django.db import models

# Create your models here.

class Members(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	pw = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name