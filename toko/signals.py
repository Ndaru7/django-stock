from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import BarangMasuk, BarangKeluar


# ====Signal barang masuk==== #
@receiver(post_save, sender=BarangMasuk)
def update_jumlah_barang_masuk(sender, instance, created, **kwargs):
    if created:
        instance.barang.qty += instance.total_barang_masuk
        instance.barang.save()

@receiver(post_delete, sender=BarangMasuk)
def delete_jumlah_barang_masuk(sender, instance, **kwargs):
    instance.barang.qty -= instance.total_barang_masuk
    instance.barang.save()

# ============================ #

# ====Signal barang keluar==== #
@receiver(post_save, sender=BarangKeluar)
def update_jumlah_barang_keluar(sender, instance, created, **kwargs):
    if created:
        instance.barang.qty -= instance.total_barang_keluar
        instance.barang.save()

@receiver(post_delete, sender=BarangKeluar)
def delete_jumlah_barang_keluar(sender, instance, **kwargs):
    instance.barang.qty += instance.total_barang_keluar
    instance.barang.save()

# ============================ #