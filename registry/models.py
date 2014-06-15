from django.db import models

# Create your models here.
class Registry(models.Model):
    _id = models.DateTimeField(auto_now_add=True)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ('_id',)
