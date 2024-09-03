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
    # if request.method == 'POST':
    #     name = request.POST.get('name', '').strip()
        
    #     try:
    #         # Gửi yêu cầu đến dịch vụ web2
    #         response = requests.post('http://localhost:8007/api/check/', data={'name': name})
    #         response.raise_for_status()  # Raise an exception for HTTP errors
            
    #         if response.status_code == 200:
    #             data = response.json()
    #             message = data.get('message', 'Unknown error')
    #         else:
    #             message = 'Error occurred while checking the name.'
    #     except requests.RequestException as e:
    #         message = f"Request failed: {e}"
        
    #     return render(request, 'check.html', {'message': message, 'name': name})
    return render(request, 'check.html')

def getHome(request):
    return render(request,'home.html')