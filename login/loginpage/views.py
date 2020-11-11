from django.db import IntegrityError

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from loginpage.models import Users


def login(request):
    if request.session.get('id', None):#类似于cookie的玩意儿,是保存在服务端的键值对
        return redirect('/login/index/')#转跳index页面
    if request.method == "GET":
        return render(request, 'login.html')
    else:#点击登陆后method为非GET
        username = request.POST.get("username")
        password = request.POST.get("password")
        res = Users.objects.filter(username = username, password = password)#查询到返回一个Users类的对象列表，0为要找的对象，未查询到返回空列表；后username为上一行自定义变量，前username为数据库内字段
        if res :
            # 把从数据库输出的字段塞入session的库中
            request.session['id'] = res[0].id
            request.session['username'] = res[0].username
            return redirect('/login/index/')
        else:
            info = "登陆失败"
        return render(request, 'temp.html', {"info":info})


def init(request):
    username = "admin"
    password = "1234"
    users = Users()
    # 向数据库中尝试保存数据
    users.username = username
    users.password = password
    try:
        users.save()
    except IntegrityError:
        return HttpResponse("用户名重复")
    return HttpResponse("OK")


def index(request):
    if request.session.get('id', None):#已经登陆过，直接进入index
        return render(request, 'index.html')
    else:
        return HttpResponse("请重新登录！")#没有登录，防止直接通过~/index/路径访问

def exit(request):#删除session数据
    if request.session.get('id', None):
        del request.session['id']
    if request.session.get('username', None):
        del request.session['username']
    return redirect('/login/login/')

def welcome(request):
    return render(request, 'welcome.html')


def ajaxlogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    res = Users.objects.filter(username=username, password=password)
    if res:
        return HttpResponse(1)
    else:
        return HttpResponse(0)
