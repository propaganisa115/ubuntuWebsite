from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
from import_export import resources
from .models import Sekolah, Provinsi, KabupatenKota, Kecamatan, Kelurahan, SekolahExtend
from django_admin_search.admin import AdvancedSearchAdmin
from .forms import SekolahSearch
from import_export.admin import ImportExportActionModelAdmin



class SekolahResource(resources.ModelResource):

    class Meta:
        model = Sekolah
        fields=('sekolah_domain','id')
        export_order = ('sekolah_domain', 'id')


class SekolahAdmin(ImportExportModelAdmin):
    list_display = [f.name for f in Sekolah._meta.fields]
    resource_class = SekolahResource

class sekolahProxy(Sekolah):
    class Meta:
        proxy = True
        verbose_name_plural = "Import Data Sekolah"



admin.site.register(sekolahProxy, SekolahAdmin)

class SekolahSearchAdmin(AdvancedSearchAdmin, SekolahAdmin ):
    list_display = [f.name for f in Sekolah._meta.fields]
    resource_class = SekolahResource
    search_form = SekolahSearch

    def sekolah_domain(request, field_value, param_values):

        query = Sekolah.objects.filter(sekolah_domain=field_value)
        return query

admin.site.register(Sekolah, SekolahSearchAdmin)



#@admin.register(models.Sekolah)

class Sekolah(admin.ModelAdmin):
    #list_display = ('sekolah_domain','sekolah_bucket','sekolah_secretKey','status')
    list_display = [f.name for f in Sekolah._meta.fields]
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

