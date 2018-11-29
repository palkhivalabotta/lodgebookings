from django.shortcuts import render
from django.http import HttpResponse


def openhomepage(request):
    type="home"
    return render(request, "home.html", {"type": type})
def UserLogin(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})

