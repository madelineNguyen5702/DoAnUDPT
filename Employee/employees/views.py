from django.shortcuts import render

# Create your views here.
# employees/views.py
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NhanVien
from .serializers import NhanVienSerializer

class LoginView(APIView):
    def post(self, request):
        ma_nv = request.data.get('MaNV')
        password = request.data.get('password')
        try:
            nhan_vien = NhanVien.objects.get(MaNV=ma_nv)
            if nhan_vien.password == password:
                # Đăng nhập thành công
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                # Mật khẩu không đúng
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except NhanVien.DoesNotExist:
            # Mã nhân viên không tồn tại
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
