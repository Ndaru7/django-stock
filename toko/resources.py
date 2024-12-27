from .models import Barang, BarangMasuk, BarangKeluar
from import_export import resources


class BarangResources(resources.ModelResource):
    class Meta:
        model = Barang
        fields = ("id", "nama_barang", "harga_barang", "satuan", "kategori", "qty")
        export_order = ("id", "nama_barang", "harga_barang", "satuan", "kategori", "qty")


class BarangMasukResources(resources.ModelResource):
    class Meta:
        model = BarangMasuk
        fields = ("id", "tanggal_masuk", "barang", "total_barang_masuk")
        export_order = ("id", "tanggal_masuk", "barang", "total_barang_masuk")


class BarangKeluarResources(resources.ModelResource):
    class Meta:
        model = BarangKeluar
        fields = ("id", "tanggal_keluar", "barang", "total_barang_keluar")
        export_order = ("id", "tanggal_keluar", "barang", "total_barang_keluar")