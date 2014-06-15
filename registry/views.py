# Create your views here.

from django.http import Http404
from registry.models import Registry
from registry.serializers import RegistrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SignUp(APIView):
    #Create a new account
    def post(self, request, format=None):
        serializer = RegistrySerializer(data = request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class RegistryDetail(APIView):
    #Retrieve a registry instance
    def get_object(self, userId):
        try:
            return Registry.objects.get(userId=userId)
        except Registry.DoesNotExist:
            raise Http404

    def get(self, request, userId, format=None):
        registry = self.get_object(userId)
        serializer = RegistrySerializer(registry)
        return Response(serializer.data)
