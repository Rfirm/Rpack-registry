from django.db import models

# Create your models here.
class Account(models.Model):
    _id = models.CharField(max_length = 36, primary_key = True)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)

    def __unicode__(self):
        return self.username
