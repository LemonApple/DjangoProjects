from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from article.models import Types, Articles


def articlelist(request):
    articles=Articles.objects.all()
    return render(request, 'article-list.html', {'articles':articles})


def articleadd(request):
    # 遍历之后types拿到的是一个列表
    if request.method == 'GET':
        types=Types.objects.all()
        # {'types':types}是添加到模板上下文的一个字典
        return render(request, 'article-add.html', {'types':types})
    else:
        title = request.POST.get("title")
        type = request.POST.get("type")
        content = request.POST.get("content")
        author = request.session.get("id")
        # 把拿到的数据写入数据库
        article = Articles(title=title, content=content, type_id=type, author_id=author)
        article.save()
        return HttpResponse("文章添加成功！")

def typeinit(request):
    type = Types(title='大陆新闻')
    type.save()
    type = Types(title='港澳台新聞')
    type.save()
    type = Types(title='US News')
    type.save()
    return render(request, 'temp.html', {"info":"文章类型初始化完成"})


def articledel(request):
    # 从ajax接收data中的id
    id=request.POST.get('id')
    # 找到对应id，通过filter会返回一个列表，第0条就是我们想要的元素，然后进行删除
    Articles.objects.filter(id=id)[0].delete()
    # 必须返回信息给ajax，否则会一直等待
    return HttpResponse("1")