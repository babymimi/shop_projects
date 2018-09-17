from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import *


def index(request):
    #获取导航菜单数据
    navigations = Navigation.objects.all()
    #分类菜单的数据
    #三个表  category
    #轮播图数据
    banners = Banner.objects.all()
    return render(request,'index.html',{'navigations':navigations})