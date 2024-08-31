from django.shortcuts import render
import requests

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Sending API")
        # Gửi yêu cầu đến API của Employee thông qua Kong Gateway
        response = requests.post('http://employee_service:8004/employee/api/employee/login/', data={'username': username, 'password': password})
        print("API Sent")
        data = response.json()
        
        # Xử lý phản hồi từ API
        if response.status_code == 200:
            return render(request, 'login_success.html', {'data': data})
        else:
            return render(request, 'login_failed.html', {'error': data.get('error', 'Unknown error')})
    
    return render(request, 'login.html')
