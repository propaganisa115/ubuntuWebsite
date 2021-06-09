from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
from import_export import resources
from .models import Sekolah, Provinsi, KabupatenKota, Kecamatan, Kelurahan


class SekolahResource(resources.ModelResource):

    class Meta:
        model = Sekolah
        fields=('sekolah_domain','id')
        export_order = ('sekolah_domain', 'id')


class SekolahAdmin(ImportExportModelAdmin):
    list_display = ('sekolah_domain','sekolah_bucket','sekolah_secretKey','status')
    resource_class = SekolahResource


admin.site.register(Sekolah, SekolahAdmin)

#@admin.register(models.Sekolah)

class Sekolah(admin.ModelAdmin):
    list_display = ('sekolah_domain','sekolah_bucket','sekolah_secretKey','status')
    readonly_fields = ('sekolah_secretKey',)

class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ('provinsi_kode','provinsi_nama')

admin.site.register(Provinsi, ProvinsiAdmin)

class KabKotaAdmin(admin.ModelAdmin):
    list_display = ('kabkota_kode','kabkota_nama')

admin.site.register(KabupatenKota, KabKotaAdmin)

class KecamatanAdmin(admin.ModelAdmin):
    list_display = ('kecamatan_kode','kecamatan_nama')

admin.site.register(Kecamatan, KecamatanAdmin)

class KelurahanAdmin(admin.ModelAdmin):
    list_display = ('kelurahan_kode','kelurahan_nama')

admin.site.register(Kelurahan, KelurahanAdmin)



