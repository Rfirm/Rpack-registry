#!/usr/bin/env python
# encoding: utf-8

from django.forms import widgets
from rest_framework import serializers
from registry.models import Registry

"""class RegistrySerializer(serializers.Serializer):
    userId = serializers.Field()
    account = serializers.CharField(widget = widgets.Textarea, max_length=20)
    password = serializers.CharField(widget = widgets.PasswordInput, max_length=20)
    email = serializers.EmailField(widget = widgets.Textarea,max_length=254)

    def restore_object(self, attrs, instance=None):
        #Create new registry
        return  Registry(**attrs)"""

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = ('id', 'account', 'password', 'email')
