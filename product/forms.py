from django import forms
from product.models import Product

class FormLogin(forms.Form):
    username = forms.CharField(label="",
                               max_length=50, 
                               widget=forms.TextInput(
                                   attrs={
                                       "placeholder": "Username",
                                   }
                                   )
                               )
    
    password = forms.CharField(label="",
                               max_length=50,
                               widget=forms.PasswordInput(
                                   attrs={
                                       "placeholder": "password",
                                   }
                               )
                               )

# class FormBarang(forms.ModelForm):
#     class Meta:
#         model = Barang
#         fields = (
#             "nama_barang",
#             "harga_barang",
#             "satuan",
#             "kategori",
#             "qty",
#         )

#         wigets = {
#             "harga_barang": forms.NumberInput(attrs={"min": "0"}),
#             "qty": forms.NumberInput(attrs={"min": "0"}),
#         }

# class FormBarangMasuk(forms.ModelForm):
#     class Meta:
#         model = BarangMasuk
#         fields = (
#             "tanggal_masuk",
#             "barang",
#             "total_barang_masuk",
#         )

#         wigets = {
#             "tanggal_masuk": forms.DateInput(attrs={"type": "date"}),
#             "total_barang_masuk": forms.NumberInput(attrs={"min": "0"}),
#         }

# class FormBarangKeluar(forms.ModelForm):
#     class Meta:
#         model = BarangKeluar
#         fields = (
#             "tanggal_keluar",
#             "barang",
#             "total_barang_keluar",
#         )

#         wigets = {
#             "tanggal_keluar": forms.DateInput(attrs={"type": "date"}),
#             "total_barang_keluar": forms.NumberInput(attrs={"min": "0"}),
#         }


# class FormatForm(forms.Form):
#     class FormatChoices(models.TextChoices):
#         XLSX = "xlsx", "xlsx"
#         CSV = "csv", "csv"
#         JSON = "json", "json"

#     format = forms.ChoiceField(choices=FormatChoices.choices)
