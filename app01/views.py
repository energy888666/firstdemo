from django.shortcuts import render,HttpResponse

# Create your views here.


def happy(request):
<<<<<<< Updated upstream
    return HttpResponse("第一次修改d")
=======
    return HttpResponse("第一次修改")
def happy2(request):
    return HttpResponse("第er次修改")
>>>>>>> Stashed changes
