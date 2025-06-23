from django.db import models
from django.utils import timezone

class Barang(models.Model):
    class SatuanChoices(models.TextChoices):
        PCS = "Pcs", "pcs"
        PACK = "Pack", "pack"
        BOX = "Box", "box"

    class KategoriChoices(models.TextChoices):
        MAKANAN = "Makanan", "makanan"
        MINUMAN = "Minuman", "minuman"

    nama_barang = models.CharField(max_length=100)
    harga_barang = models.PositiveIntegerField(default=0)
    satuan = models.CharField(max_length=20, choices=SatuanChoices.choices)
    kategori = models.CharField(max_length=20, choices=KategoriChoices.choices)
    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama_barang
    

class BarangMasuk(models.Model):
    tanggal_masuk = models.DateField(default=timezone.now)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    total_barang_masuk = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.barang.nama_barang
    
    
class BarangKeluar(models.Model):
    tanggal_keluar = models.DateField(default=timezone.now)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    total_barang_keluar = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.barang.nama_barang