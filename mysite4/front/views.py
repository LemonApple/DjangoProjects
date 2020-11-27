from django.shortcuts import render

# Create your views here.
from article.models import Types, Articles


def default(request):
    types = Types.objects.all()
    return render(request, 'default.html', {'types': types})


def types(request):
    id = request.GET.get('id')
    articles = Articles.objects.filter(type_id=id)
    return render(request, 'front-types.html', {'articles': articles})


def articles(request):
    id = request.GET.get('id')
    article = Articles.objects.filter(id=id)[0]
    return render(request, 'font-article.html', {'article': article})