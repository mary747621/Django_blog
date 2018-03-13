from django.shortcuts import render

# Create your views here.

# Hello world

from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
    return render(request,"hello_world.html",{
        'current_time':str(datetime.now()),
    })
#若想新增現在時間或其他東西，記得要去hello_world.html新增
#注意括號的使用！
