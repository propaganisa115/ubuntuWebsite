from django.db import models
from django.utils.crypto import get_random_string


class Sekolah(models.Model):
	STATUS_CHOICES = (
		('Client','client'),
		('Demo','demo'),
	)
	sekolah_domain=models.CharField(max_length=100)
	sekolah_bucket=models.CharField(max_length=200,blank=True)
	sekolah_secretKey=models.CharField(max_length=10,unique=True,editable=False)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES ,default='Client')

	def save(self, *args,**kwargs):
		self.sekolah_secretKey=get_random_string(length=9)
		super(Sekolah, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Daftar Sekolah"

class Provinsi(models.Model):
	provinsi_kode=models.CharField(max_length=100, unique=True)
	provinsi_nama=models.CharField(max_length=300,blank=True)

	def __str__(self):
		return self.provinsi_nama

	class Meta:
		verbose_name_plural = "Provinsi"

class KabupatenKota(models.Model):
	kabkota_kode=models.CharField(max_length=100, unique=True)
	kabkota_nama=models.CharField(max_length=300,blank=True)
	provinsi= models.ForeignKey(Provinsi, on_delete=models.CASCADE)

	def __str__(self):
		return self.kabkota_nama

	class Meta:
		verbose_name_plural = "Kabupaten Kota"

class Kecamatan(models.Model):
	kecamatan_kode=models.CharField(max_length=100, unique=True)
	kecamatan_nama=models.CharField(max_length=300,blank=True)
	KabupatenKota = models.ForeignKey(KabupatenKota, on_delete=models.CASCADE)

	def __str__(self):
		return self.kecamatan_nama

	class Meta:
		verbose_name_plural = "Kecamatan"

class Kelurahan(models.Model):
	kelurahan_kode=models.CharField(max_length=100, unique=True)
	kelurahan_nama=models.CharField(max_length=300,blank=True)
	Kecamatan = models.ForeignKey(Kecamatan, on_delete=models.CASCADE)

	def __str__(self):
		return self.kelurahan_nama

	class Meta:
		verbose_name_plural = "Kelurahan"