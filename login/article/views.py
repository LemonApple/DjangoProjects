from django.shortcuts import render, redirect


# Create your views here.
def articlelist(request):
    if request.session.get('id'):
        return render(request, 'article-list.html')
    else:
        return redirect('/login/login/')