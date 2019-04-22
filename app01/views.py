from django.shortcuts import render,HttpResponse

# Create your views here.


def happy(request):
    return HttpResponse("第一次修改d")
def happy2(request):
    return HttpResponse("第er次修改")
