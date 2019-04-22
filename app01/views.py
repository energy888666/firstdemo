from django.shortcuts import render,HttpResponse

# Create your views here.


def happy(request):
<<<<<<< Updated upstream
    return HttpResponse("第一次修改dea")
=======
    return HttpResponse("第一次修改")
def happy2(request):
    return HttpResponse("第2次修改")
>>>>>>> Stashed changes
