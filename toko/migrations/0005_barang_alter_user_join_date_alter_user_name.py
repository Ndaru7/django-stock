# Generated by Django 5.1.2 on 2024-10-25 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0004_alter_user_join_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_barang', models.PositiveIntegerField(unique=True)),
                ('nama_barang', models.CharField(max_length=100)),
                ('qty', models.IntegerField(default=0)),
                ('harga_barang', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 26, 1, 54, 5, 183687)),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='nama', max_length=30),
        ),
    ]
