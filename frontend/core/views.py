from django.shortcuts import render
from rest_framework.views import APIView
from core.models import NhanVien  # Đảm bảo rằng bạn đã import đúng model
import requests
class LoginView(APIView):
    def get(self, request):
        # Truy vấn tất cả các bản ghi từ bảng NhanVien
        nhanvien_list = NhanVien.objects.all()
        
        # Render template với dữ liệu
        context = {'nhanviens': nhanvien_list}
        return render(request, 'api.html', context)

def check_name(request):
    return render(request, 'check.html')

def getHome(request):
    return render(request,'home.html')

def getEmployeeHome(request):
    return render(request,'employee/home.html')

def getManagerHome(request):
    return render(request,'manager/home.html')

def getLogin(request):
    return render(request,'login.html')