from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("dashboard/", views.DashboardTemplateView.as_view(), name="dashboard"),
    path("auth/login/", views.LoginFormView.as_view(), name="login"),
    path("auth/logout/", views.LogoutTemplateView.as_view(), name="logout"),

    path("product/", views.ProductListView.as_view(), name="product-list"),
    path("product/detail/<int:pk>", views.ProductDetailView.as_view(), name="product-detail"),
    path("product/add/", views.ProductAddView.as_view(), name="product-add"),
    path("product/update/<int:pk>/", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/delete/<int:pk>/", views.ProductDeleteView.as_view(), name="product-delete"),
    #path("barang/cetak_laporan", views.CetakBarangListView.as_view(), name="cetak-barang"),

    # # Url Barang Masuk 
    # path("barang_masuk/", views.barang_masuk, name="barang-masuk"),
    # path("barang_masuk/tambah_barang_masuk/", views.tambah_barang_masuk, name="tambah-barang-masuk"),
    # path("barang_masuk/update_barang_masuk/<int:id>/", views.update_barang_masuk, name="update-barang-masuk"),
    # path("barang_masuk/delete_barang_masuk/<int:id>/", views.delete_barang_masuk, name="delete-barang-masuk"),
    # path("barang_masuk/cetak_laporan", views.CetakBarangMasukListView.as_view(), name="cetak-barang-masuk"),

    # # Url Barang Keluar
    # path("barang_keluar/", views.barang_keluar, name="barang-keluar"),
    # path("barang_keluar/tambah_barang_keluar", views.tambah_barang_keluar, name="tambah-barang-keluar"),
    # path("barang_keluar/update_barang_keluar/<int:id>", views.update_barang_keluar, name="update-barang-keluar"),
    # path("barang_keluar/delete_barang_keluar/<int:id>", views.delete_barang_keluar, name="delete-barang-keluar"),
    # path("barang_keluar/cetak_laporan", views.CetakBarangKeluarListView.as_view(), name="cetak-barang-keluar"),

    
    # path("logout/", views.logout_user, name="logout"),
]

handler404 = "product.views.handling_404"