from rest_framework import serializers 
from .models import Sekolah, Provinsi, KabupatenKota, Kecamatan, Kelurahan

class SekolahSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sekolah
		fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sekolah
        fields = ('sekolah_domain','sekolah_bucket')

class ProvinsiSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provinsi
		fields = '__all__'
		depth = 1

class KabupatenKotaSerializer(serializers.ModelSerializer):

	class Meta:
		model = KabupatenKota
		fields = '__all__'
		depth = 1

class KecamatanSerializer(serializers.ModelSerializer):

	class Meta:
		model = Kecamatan
		fields = '__all__'
		depth = 1

class KelurahanSerializer(serializers.ModelSerializer):

	class Meta:
		model = Kelurahan
		fields = '__all__'
		depth = 1

