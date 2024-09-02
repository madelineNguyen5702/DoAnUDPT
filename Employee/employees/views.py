from django.shortcuts import render

# # Create your views here.
# # employees/views.py
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NhanVien
from .serializers import NhanVienSerializer

# class LoginView(APIView):
#     def get(self, request):
#         # Xử lý yêu cầu GET
#         return Response({"message": "GET method is not allowed for login"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#     # def post(self, request):
#     #     ma_nv = request.data.get('MaNV')
#     #     password = request.data.get('MatKhau')
#     #     try:
#     #         nhan_vien = NhanVien.objects.get(MaNV=ma_nv)
#     #         if nhan_vien.password == password:
#     #             # Đăng nhập thành công
#     #             return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#     #         else:
#     #             # Mật khẩu không đúng
#     #             return Response({"error": "Mật khẩu không đúng"}, status=status.HTTP_400_BAD_REQUEST)
#     #     except NhanVien.DoesNotExist:
#     #         # Mã nhân viên không tồn tại
#     #         return Response({"error": "Mã nhân viên không tồn tại"}, status=status.HTTP_400_BAD_REQUEST)

#     def post(self, request):
#         ma_nv = request.data.get('MaNV')
#         password = request.data.get('password')

#         try:
#             nhan_vien = NhanVien.objects.get(MaNV=ma_nv)
            
#             # So sánh mật khẩu
#             if nhan_vien.MatKhau == password:
#                 # Đăng nhập thành công
#                 return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#             else:
#                 # Mật khẩu không đúng
#                 return Response({"error": "Mật khẩu không đúng"}, status=status.HTTP_400_BAD_REQUEST)
#         except NhanVien.DoesNotExist:
#             # Mã nhân viên không tồn tại
#             return Response({"error": "Mã nhân viên không tồn tại"}, status=status.HTTP_400_BAD_REQUEST)

# views.py in employee_service

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import NhanVien
from .serializers import NhanVienSerializer

class LoginView(APIView):
    def get(self, request):
        # Lấy tất cả các bản ghi từ bảng NhanVien
        nhan_vien_list = NhanVien.objects.all()
        # Chuyển đổi danh sách đối tượng thành định dạng JSON
        serializer = NhanVienSerializer(nhan_vien_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Lấy dữ liệu từ request
        username = request.data.get('MaNV')
        password = request.data.get('MatKhau')

        # Kiểm tra xem username có tồn tại không
        try:
            nhan_vien = NhanVien.objects.get(MaNV=username)
        except NhanVien.DoesNotExist:
            return Response({"error": "Invalid username"}, status=status.HTTP_400_BAD_REQUEST)

        # So sánh mật khẩu
        if nhan_vien.MatKhau == password:
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
