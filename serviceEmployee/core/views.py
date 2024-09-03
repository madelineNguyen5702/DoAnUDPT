from django.shortcuts import render
from rest_framework.views import APIView
from core.models import NhanVien  # Đảm bảo rằng bạn đã import đúng model
from rest_framework.response import Response
from rest_framework import status
from django.contrib.sessions.models import Session


class LoginView(APIView):
    def get(self, request):
        # Truy vấn tất cả các bản ghi từ bảng NhanVien
        nhanvien_list = NhanVien.objects.all()
        
        # Render template với dữ liệu
        context = {'nhanviens': nhanvien_list}
        return render(request, 'api.html', context)

class CheckNhanVienView(APIView):
    def get(self, request):
        MaNV = request.data.get('MaNV')
        exists = NhanVien.objects.filter(MaNV=MaNV).exists()
        if NhanVien.objects.filter(MaNV=MaNV).exists():
            message = f"Tên '{MaNV}' có sẵn (available)."
        else:
            message = f"Tên '{MaNV}' không tồn tại (not available)."
        return Response({'message': message}, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        ma_nv = data.get('MaNV', '').strip()
        mat_khau = data.get('MatKhau', '').strip()

        # Kiểm tra dữ liệu có tồn tại trong cơ sở dữ liệu
        if NhanVien.objects.filter(MaNV=ma_nv).exists():
            if NhanVien.objects.filter(MatKhau=mat_khau).exists():
                message = f"Authenticated"
            else:
                message = f"Mật khẩu không đúng"
        else:
            message = f"Tên '{ma_nv}' không tồn tại (not available)."

        return Response({'message': message}, status=status.HTTP_200_OK)
    
