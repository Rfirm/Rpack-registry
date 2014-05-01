from django.db import models

# Create your models here.

class Package(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=200)
	owner = models.CharField(max_length=200)
	url = models.URLField()
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.name
