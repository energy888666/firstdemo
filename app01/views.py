from django.shortcuts import render,HttpResponse

# Create your views here.


def happy(request):
    return HttpResponse("第一次修改")
