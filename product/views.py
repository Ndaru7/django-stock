from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from .forms import FormLogin


class DashboardTemplateView(generic.TemplateView):
    template_name = "dashboard.html"

class LoginFormView(generic.FormView):
    template_name = "login.html"
    form_class = FormLogin
    success_url = "/dashboard/"
    
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Login berhasil!")

            return self.form_valid(form)
        
        else:
            return self.form_invalid(form)
        

class LogoutTemplateView(generic.TemplateView):
    template_name = "logout.html"

    def post(self, request):
        logout(request)
        return redirect("product:login")

# def is_valid_query(param):
#     return param != "" and param is not None

# def index(request):
#     form = FormLogin()

#     if request.method == "POST":
#         form = FormLogin(request.POST)
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Berhasil Login !", extra_tags="success")
#             return redirect("dashboard")
#         else:
#             messages.error(request, "Terjadi keslahan, login ulang!")
#             return redirect("index")
        
#     context = {
#             "title": "Index | Django",
#             "form": form,
#         }
#     return render(request, "index.html", context)

# def logout_user(request):
#     logout(request)
#     messages.success(request, "Logout berhasil!")
#     return redirect("index")

# # ===== Area CRUD Barang ===== #

# @login_required(login_url="/")
# def barang(request):
#     data = Barang.objects.all()

#     paginator = Paginator(data, 25)
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)

#     nama_barang = request.GET.get("nama_barang")

#     if is_valid_query(nama_barang):
#         data = data.filter(nama_barang__icontains=nama_barang)

#     context = {
#         "title": "Django | Data Barang",
#         "data": data,
#         "page_obj": page_obj,
#     }
#     return render(request, "barang/barang.html", context)

# @login_required(login_url="/")
# def tambah_barang(request):
#     data = Barang.objects.all()
#     form = FormBarang()

#     if request.method == "POST":
#         form = FormBarang(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Barang berhasil ditambahkan!")
#             return redirect("barang")

#     context = {
#         "title": "Django | Tambah Barang",
#         "data": data,
#         "form": form,
#     }
#     return render(request, "barang/tambah_barang.html", context)

# @login_required(login_url="/")
# def update_barang(request, id):
#     data = Barang.objects.get(id=id)
#     form = FormBarang(instance=data)

#     if request.method == "POST":
#         form = FormBarang(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
            
#             messages.success(request, "Barang berhasil diupdate!")
#             return redirect("barang")
        
#     context = {
#         "title": "Django | Update Barang",
#         "pk": data,
#         "form": form,
#     }
#     return render(request, "barang/update_barang.html", context)

# @login_required(login_url="/")
# def delete_barang(request, id):
#     data = Barang.objects.get(id=id)
#     if request.method == "POST":
#         data.delete()
#         messages.success(request, "Barang berhasil dihapus!")
#         return redirect("barang")

#     context = {
#         "title": "Django | Delete Barang",
#         "data": data,
#     }
#     return render(request, "barang/delete_barang.html", context)


# class CetakBarangListView(ListView, FormView):
#     model = Barang
#     template_name = "barang/cetak_barang.html"
#     form_class = FormatForm

#     def post(self, request, **kwargs):
#         qs = self.get_queryset()
#         dataset = BarangResources().export(qs)
#         format = request.POST.get("format")

#         if format == "xlsx":
#             ds = dataset.xlsx
#         elif format == "csv":
#             ds = dataset.csv
#         else:
#             ds = dataset.json

#         response = HttpResponse(ds, content_type=f"{format}")
#         response["Content-Disposition"] = f"attachment; filename=laporan.{format}"
#         return response

# # ================================== #

# # ===== Area CRUD Barang masuk ===== #

# @login_required(login_url="/")
# def barang_masuk(request):
#     data = BarangMasuk.objects.all()
#     paginator = Paginator(data, 25)
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)

#     tanggal_min = request.GET.get("tanggal_min")
#     tanggal_max = request.GET.get("tanggal_max")

#     if is_valid_query(tanggal_min):
#         data = data.filter(tanggal_masuk__gte=tanggal_min)

#     if is_valid_query(tanggal_max):
#         data = data.filter(tanggal_masuk__lte=tanggal_max)

#     context = {
#         "title": "Django | Data Barang Masuk",
#         "data": data,
#         "page_obj": page_obj,
#     }
#     return render(request, "barang_masuk/barang_masuk.html", context)

# @login_required(login_url="/")
# def tambah_barang_masuk(request):
#     data = BarangMasuk.objects.all()
#     form = FormBarangMasuk()

#     if request.method == "POST":
#         form = FormBarangMasuk(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Barang masuk berhasil ditambahkan!")
#             return redirect("barang-masuk")

#     context = {
#         "title": "Django | Tambah Barang Masuk",
#         "data": data,
#         "form": form,
#     }
#     return render(request, "barang_masuk/tambah_barang_masuk.html", context)

# @login_required(login_url="/")
# def update_barang_masuk(request, id):
#     data = BarangMasuk.objects.get(id=id)
#     form = FormBarangMasuk(instance=data)

#     if request.method == "POST":
#         form = FormBarangMasuk(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
            
#             messages.success(request, "Barang masuk berhasil diupdate!")
#             return redirect("barang-masuk")
        
#     context = {
#         "title": "Django | Update Barang Masuk",
#         "pk": data,
#         "form": form,
#     }
#     return render(request, "barang_masuk/update_barang_masuk.html", context)
        
# @login_required(login_url="/")
# def delete_barang_masuk(request, id):
#     data = BarangMasuk.objects.get(id=id)
#     if request.method == "POST":
#         data.delete()
#         messages.success(request, "Barang masuk berhasil dihapus!")
#         return redirect("barang-masuk")

#     context = {
#         "title": "Django | Delete Barang Masuk",
#         "data": data,
#     }
#     return render(request, "barang_masuk/delete_barang_masuk.html", context)


# class CetakBarangMasukListView(ListView, FormView):
#     model = BarangMasuk
#     template_name = "barang_masuk/cetak_barang_masuk.html"
#     form_class = FormatForm

#     def post(self, request, **kwargs):
#         qs = self.get_queryset()
#         dataset = BarangMasukResources().export(qs)
#         format = request.POST.get("format")

#         if format == "xlsx":
#             ds = dataset.xlsx
#         elif format == "csv":
#             ds = dataset.csv
#         else:
#             ds = dataset.json

#         response = HttpResponse(ds, content_type=f"{format}")
#         response["Content-Disposition"] = f"attachment; filename=laporan.{format}"
#         return response
# # =========================================================================================== #

# # ===== Area CRUD Barang keluar ===== #

# @login_required(login_url="/")
# def barang_keluar(request):
#     data = BarangKeluar.objects.all()
#     paginator = Paginator(data, 25)
#     page_number = request.GET.get("page", 1)
#     page_obj = paginator.get_page(page_number)

#     tanggal_min = request.GET.get("tanggal_min")
#     tanggal_max = request.GET.get("tanggal_max")

#     if is_valid_query(tanggal_min):
#         data = data.filter(tanggal_keluar__gte=tanggal_min)

#     if is_valid_query(tanggal_max):
#         data = data.filter(tanggal_keluar__lte=tanggal_max)

#     context = {
#         "title": "Django | Data Barang Keluar",
#         "data": data,
#         "page_obj": page_obj,
#     }
#     return render(request, "barang_keluar/barang_keluar.html", context)

# @login_required(login_url="/")
# def tambah_barang_keluar(request):
#     data = BarangKeluar.objects.all()
#     form = FormBarangKeluar()
#     if request.method == "POST":
#         form = FormBarangKeluar(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Barang Keluar berhasil ditambahkan!")
#             return redirect("barang-keluar")

#     context = {
#         "title": "Django | Tambah Barang Keluar",
#         "data": data,
#         "form": form,
#     }
#     return render(request, "barang_keluar/tambah_barang_keluar.html", context)

# @login_required(login_url="/")
# def update_barang_keluar(request, id):
#     data = BarangKeluar.objects.get(id=id)
#     form = FormBarangKeluar(instance=data)
#     if request.method == "POST":
#         form = FormBarangKeluar(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Barang Masuk berhasil diupdate!")
#             return redirect("barang-keluar")
        
#     context = {
#         "title": "Django | Update Barang Keluar",
#         "data": data,
#         "form": form,
#     }
#     return render(request, "barang_keluar/update_barang_keluar.html", context)

# @login_required(login_url="/")
# def delete_barang_keluar(request, id):
#     data = BarangKeluar.objects.get(id=id)
#     if request.method == "POST":
#         data.delete()
#         messages.success(request, "Barang Keluar berhasil dihapus!")
#         return redirect("barang-keluar")
#     context = {
#         "title": "Django | Delete Barang Keluar",
#         "data": data
#     }
#     return render(request, "barang_keluar/delete_barang_keluar.html", context)


# class CetakBarangKeluarListView(ListView, FormView):
#     model = BarangKeluar
#     template_name = "barang_keluar/cetak_barang_keluar.html"
#     form_class = FormatForm

#     def post(self, request, **kwargs):
#         qs = self.get_queryset()
#         dataset = BarangKeluarResources().export(qs)
#         format = request.POST.get("format")

#         if format == "xlsx":
#             ds = dataset.xlsx
#         elif format == "csv":
#             ds = dataset.csv
#         else:
#             ds = dataset.json

#         response = HttpResponse(ds, content_type=f"{format}")
#         response["Content-Disposition"] = f"attachment; filename=laporan.{format}"
#         return response
# # =========================================================================================== #

# def handling_404(request, exception):
#     context = {
        
#     }
#     return render(request, "404.html", context)