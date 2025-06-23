from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Url Barang
    path("barang/", views.barang, name="barang"),
    path("barang/tambah_barang/", views.tambah_barang, name="tambah-barang"),
    path("barang/update_barang/<int:id>/", views.update_barang, name="update-barang"),
    path("barang/delete_barang/<int:id>/", views.delete_barang, name="delete-barang"),
    path("barang/cetak_laporan", views.CetakBarangListView.as_view(), name="cetak-barang"),

    # Url Barang Masuk 
    path("barang_masuk/", views.barang_masuk, name="barang-masuk"),
    path("barang_masuk/tambah_barang_masuk/", views.tambah_barang_masuk, name="tambah-barang-masuk"),
    path("barang_masuk/update_barang_masuk/<int:id>/", views.update_barang_masuk, name="update-barang-masuk"),
    path("barang_masuk/delete_barang_masuk/<int:id>/", views.delete_barang_masuk, name="delete-barang-masuk"),
    path("barang_masuk/cetak_laporan", views.CetakBarangMasukListView.as_view(), name="cetak-barang-masuk"),

    # Url Barang Keluar
    path("barang_keluar/", views.barang_keluar, name="barang-keluar"),
    path("barang_keluar/tambah_barang_keluar", views.tambah_barang_keluar, name="tambah-barang-keluar"),
    path("barang_keluar/update_barang_keluar/<int:id>", views.update_barang_keluar, name="update-barang-keluar"),
    path("barang_keluar/delete_barang_keluar/<int:id>", views.delete_barang_keluar, name="delete-barang-keluar"),
    path("barang_keluar/cetak_laporan", views.CetakBarangKeluarListView.as_view(), name="cetak-barang-keluar"),

    
    path("logout/", views.logout_user, name="logout"),
]

handler404 = "product.views.handling_404"