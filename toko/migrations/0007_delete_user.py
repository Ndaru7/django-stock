# Generated by Django 5.1.2 on 2024-11-08 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0006_barang_desc_barang_kategori_barang_satuan_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
