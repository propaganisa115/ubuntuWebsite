from rest_framework import generics
from rest_framework.response import Response
from .serializer import SekolahSerializer, AuthSerializer
from .models import Sekolah
from rest_framework.permissions import IsAuthenticated
from .authentication import SekolahAuthentication


class SekolahCreateApi(generics.CreateAPIView):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer


class SekolahApi(SekolahAuthentication, generics.ListAPIView):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer


class SekolahUpdateApi(SekolahAuthentication, generics.RetrieveUpdateAPIView):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer


class SekolahAuthApi(SekolahAuthentication, generics.ListAPIView):
    serializer_class = AuthSerializer

    def get_queryset(self): 
        queryset_list = Sekolah.objects.all()
        secretkey = self.request.META.get('HTTP_SECRETKEY')
        if secretkey:
            queryset_list = queryset_list.filter(sekolah_secretKey=secretkey)
        return queryset_list


class SekolahDeleteApi(SekolahAuthentication, generics.DestroyAPIView):
    queryset = Sekolah.objects.all()
    serializer_class = SekolahSerializer
