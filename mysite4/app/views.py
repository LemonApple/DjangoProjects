from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def cal(request):
    return render(request, "cal.html")


def cal2(request):
    num1 = request.POST.get("num1")
    num2 = request.POST.get("num2")
    return HttpResponse(int(num1)+int(num2))