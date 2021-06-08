from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models
from import_export import resources
from .models import Sekolah


class SekolahResource(resources.ModelResource):

    class Meta:
        model = Sekolah
        fields=('sekolah_domain','id')
        export_order = ('sekolah_domain', 'id')


class SekolahAdmin(ImportExportModelAdmin):
    list_display = ('id','sekolah_domain','sekolah_bucket','sekolah_secretKey','status')
    resource_class = SekolahResource


admin.site.register(Sekolah, SekolahAdmin)

#@admin.register(models.Sekolah)

class Sekolah(admin.ModelAdmin):
    list_display = ('sekolah_domain','sekolah_bucket','sekolah_secretKey','status')
    readonly_fields = ['sekolah_secretKey']
