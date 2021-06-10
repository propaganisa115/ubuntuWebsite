from django.urls import path
from .api import \
	SekolahCreateApi, SekolahApi, SekolahUpdateApi, SekolahDeleteApi, \
	SekolahAuthApi, ProvinsiAPI, ProvinsiAPIdetails,KabupatenKotaAPI,\
	KabupatenKotadetails, KecamatanAPI,Kecamatandetails, KelurahanAPI,\
	Kelurahandetails


urlpatterns = [
	#path('create', SekolahCreateApi.as_view()),
	#path('', SekolahApi.as_view()),
	#path('<int:pk>', SekolahUpdateApi.as_view()),
	path('auth', SekolahAuthApi.as_view()),
	#path('delete/<int:pk>', SekolahDeleteApi.as_view()),
	path('list-provinsi', ProvinsiAPI.as_view()),
    path('provinsi/<str:provinsi_kode>', ProvinsiAPIdetails.as_view()),
    path('list-kabupatenkota/<str:provinsi_kode>', KabupatenKotaAPI.as_view()),
	path('kabupatenkota/<str:kabkota_kode>', KabupatenKotadetails.as_view()),
	path('list-kecamatan/<str:kabkota_kode>', KecamatanAPI.as_view()),
	path('kecamatan/<str:kecamatan_kode>', Kecamatandetails.as_view()),
    path('list-kelurahan/<str:kecamatan_kode>', KelurahanAPI.as_view()),
    path('kelurahan/<str:kelurahan_kode>', Kelurahandetails.as_view()),
]