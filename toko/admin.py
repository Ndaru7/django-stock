from django.contrib import admin
from .models import Barang, BarangMasuk, BarangKeluar

admin.site.register(Barang)
admin.site.register(BarangMasuk)
admin.site.register(BarangKeluar)