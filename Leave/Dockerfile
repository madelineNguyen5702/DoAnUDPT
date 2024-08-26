# Sử dụng image Python chính thức làm cơ sở
FROM python:3.12

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào thư mục làm việc
COPY requirements.txt requirements.txt

# Cài đặt các phụ thuộc
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào thư mục làm việc
COPY . .

# Cung cấp port mà ứng dụng sẽ chạy trên container
EXPOSE 8000

# Chạy server Gunicorn khi container được khởi động
CMD ["gunicorn", "Leave.wsgi:application", "--bind", "0.0.0.0:8000"]
