from django.db import models
from django.utils.crypto import get_random_string


class Sekolah(models.Model):
	STATUS_CHOICES = (
		('Client','client'),
		('Demo','demo'),
	)
	sekolah_domain=models.CharField(max_length=100)
	sekolah_bucket=models.CharField(max_length=200)
	sekolah_secretKey=models.CharField(max_length=10,unique=True,editable=False)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES ,default='Client')

	def save(self, *args,**kwargs):
		self.sekolah_secretKey=get_random_string(length=9)
		super(Sekolah, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = "Daftar Sekolah"
