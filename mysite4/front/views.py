from django.shortcuts import render

# Create your views here.
from article.models import Types, Articles


def default(request):
    return render(request, 'default.html')

def types(request):
    id = request.GET.get('id')
    articles = Articles.objects.filter(type_id=id)
    return render(request, 'front-types.html', {'articles': articles})