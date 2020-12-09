import os

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from article.models import Types, Articles
from mysite4.settings import BASE_DIR
import datetime

def articlelist(request):
    articles = Articles.objects.all()
    return render(request, 'article-list.html', {'articles': articles})


def articleadd(request):
    if request.method == 'GET':
        types = Types.objects.all()
        print(types)
        return render(request, 'article-add.html', {'types': types})
    else:
        title = request.POST.get("title")
        type = request.POST.get("type")
        content = request.POST.get("content")
        author = request.session.get("id")
        myfile = request.FILES.get("myfile")
        myfile_path = os.path.join(BASE_DIR, 'static', 'upload', myfile.name)

        newfilename = str (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        newfilename2 = myfile.name
        ext = newfilename2.split('.')[-1]
        newfilename = newfilename + "." + ext
        myfile_path = os.path.join(BASE_DIR, 'static', 'upload', newfilename)
        with open(myfile_path, 'wb') as f:
            for chunk in myfile.chunks():
                f.write(chunk)
        upload_location = os.path.join('upload', newfilename)
    article = Articles(title=title, content=content, type_id=type, author_id=author, fujian=upload_location)
    article.save()
    return HttpResponse("文章添加成功！")


def typeinit(request):
    type = Types(title='中国新闻')
    type.save()
    type = Types(title='港澳台新闻')
    type.save()
    type = Types(title='美国新闻')
    type.save()
    type = Types(title='娱乐新闻')
    type.save()
    type = Types(title='科技新闻')
    type.save()
    type = Types(title='财经新闻')
    type.save()
    return render(request, 'temp.html', {"info": "文章类型初始化完成！"})


def articledel(request):
    id = request.POST.get('id')
    Articles.objects.filter(id=id)[0].delete()
    return HttpResponse("1")


def articleedit(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        article = Articles.objects.filter(id=id)[0]
        types = Types.objects.all()
        return render(request, 'article-edit.html', {'article': article, 'types': types})
    else:
        title = request.POST.get("title")
        type = request.POST.get("type")
        content = request.POST.get("content")
        id = request.POST.get('id')
        author = request.session.get("id")
        article = Articles.objects.filter(id=id)[0]
        article.title = title
        article.type_id = type
        article.author_id = author
        article.content = content
        article.save()
        return HttpResponse("修改成功！")
