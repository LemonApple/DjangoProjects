from django.shortcuts import render, redirect


# Create your views here.
from article.models import Types


def articlelist(request):
    if request.session.get('id'):
        return render(request, 'article-list.html')
    else:
        return redirect('/login/login/')


def articleadd(request):
    return render(request, 'article-add.html')


def typeinit(request):
    type = Types(title='大陆新闻')
    type.save()
    type = Types(title='港澳台新聞')
    type.save()
    type = Types(title='US News')
    type.save()
    return render(request, 'temp.html', {"info":"文章类型初始化完成"})