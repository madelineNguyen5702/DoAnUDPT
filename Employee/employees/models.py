from django.db import models

# Create your models here.
class NhanVien(models.Model):
    MaNV = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.MaNV