from rest_framework import generics
from rest_framework.response import Response
from .serializer import SekolahSerializer, AuthSerializer, ProvinsiSerializer,\
    KabupatenKotaSerializer, KecamatanSerializer, KelurahanSerializer
from .models import Sekolah, Provinsi, KabupatenKota, Kecamatan, Kelurahan
from rest_framework.permissions import IsAuthenticated
from .authentication import SekolahAuthentication
from django.shortcuts import get_object_or_404


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


class ProvinsiAPI(generics.ListAPIView):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer


class ProvinsiAPIdetails(generics.RetrieveAPIView):
    queryset = Provinsi.objects.all()
    serializer_class = ProvinsiSerializer

    def retrieve(self, request, provinsi_kode):
        queryset = Provinsi.objects.all()
        provinsi_kode = get_object_or_404(queryset, provinsi_kode=provinsi_kode)
        serializer = ProvinsiSerializer(provinsi_kode)
        return Response(serializer.data)

class KabupatenKotaAPI(generics.ListAPIView):
    #queryset = KabupatenKota.objects.all()
    serializer_class = KabupatenKotaSerializer

    def get_queryset(self):
        return KabupatenKota.objects.filter(provinsi__provinsi_kode= self.kwargs.get('provinsi_kode'))

class KabupatenKotadetails(generics.RetrieveAPIView):
    queryset = KabupatenKota.objects.all()
    serializer_class = KabupatenKotaSerializer

    def retrieve(self, request, kabkota_kode):
        queryset = KabupatenKota.objects.all()
        kabkota_kode = get_object_or_404(queryset, kabkota_kode=kabkota_kode)
        serializer = KabupatenKotaSerializer(kabkota_kode)
        return Response(serializer.data)

class KecamatanAPI(generics.ListAPIView):
    #queryset = KabupatenKota.objects.all()
    serializer_class = KecamatanSerializer

    def get_queryset(self):
        return Kecamatan.objects.filter(KabupatenKota__kabkota_kode= self.kwargs.get('kabkota_kode'))

class Kecamatandetails(generics.RetrieveAPIView):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializer

    def retrieve(self, request, kecamatan_kode):
        queryset = Kecamatan.objects.all()
        kecamatan_kode = get_object_or_404(queryset, kecamatan_kode=kecamatan_kode)
        serializer = KecamatanSerializer(kecamatan_kode)
        return Response(serializer.data)

class KelurahanAPI(generics.ListAPIView):
    #queryset = KabupatenKota.objects.all()
    serializer_class = KelurahanSerializer

    def get_queryset(self):
        return Kelurahan.objects.filter(Kecamatan__kecamatan_kode= self.kwargs.get('kecamatan_kode'))

class Kelurahandetails(generics.RetrieveAPIView):
    queryset = Kelurahan.objects.all()
    serializer_class = KelurahanSerializer

    def retrieve(self, request, kelurahan_kode):
        queryset = Kelurahan.objects.all()
        kelurahan_kode = get_object_or_404(queryset, kelurahan_kode=kelurahan_kode)
        serializer = KelurahanSerializer(kelurahan_kode)
        return Response(serializer.data)