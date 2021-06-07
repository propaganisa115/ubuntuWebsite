from rest_framework import serializers 
from .models import Sekolah

class SekolahSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sekolah
		fields = '__all__'


class AuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sekolah
        fields = ('sekolah_domain','sekolah_bucket')