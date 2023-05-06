from django.contrib import admin

# Register your models here.
# 这里要注意在models前加一个. 表示是当前目录
from .models import Book,Author,UserInfo

admin.site.register([Book,Author,UserInfo])