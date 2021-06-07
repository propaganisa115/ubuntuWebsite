from django.contrib import admin
from . import models

@admin.register(models.Sekolah)
class Sekolah(admin.ModelAdmin):
    list_display = ('sekolah_domain','sekolah_bucket','sekolah_secretKey')
    readonly_fields = ['sekolah_secretKey']



