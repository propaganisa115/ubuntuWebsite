from .models import Sekolah
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.http import HttpResponse

class SekolahAuthentication():
    def dispatch(self, request, *args, **kwargs): 
        print('dispacth')
        secretKey = request.META.get('HTTP_SECRETKEY')
        
        if not secretKey: # no username passed in request headers
            return HttpResponse('Unauthorized', status=401)
        try:
            secret = Sekolah.objects.get(sekolah_secretKey=secretKey) # get the user
        except Sekolah.DoesNotExist:
            return HttpResponse('authorization key is invalid', status=401)

        return super().dispatch(request, *args, **kwargs)