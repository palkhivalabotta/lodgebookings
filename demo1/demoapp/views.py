from django.shortcuts import render
from django.http import HttpResponse
from .models import register
from .models import feedback

#=====================HOME PAGE======================================
def openhomepage(request):
    type="home"
    return render(request, "home.html", {"type": type})
def UserLogin(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})
def booking(request):
    type = request.GET.get("type")
    return render(request,"home.html",{"type":type})
def gallary(request):
    type =request.GET.get("type")
    return render(request,"home.html",{"type":type})
def Register(request):
    type = request.GET.get("type")
    return render(request, "home.html", {"type": type})
def contact(request):
    type = request.GET.get("type")
    return render(request, "home.html")
#=============================USER REGISTER PAGE===================================================
def insertdetails(request):
    #type =request.GET.get("type")
    name = request.POST['name']
    cno = request.POST['cno']
    email = request.POST['email']
    password = request.POST['pass']

    #print(u_name,u_cno,u_email,u_pass)

    dr = register(username=name,contact_no=cno,email_id=email,password=password)
    dr.save()
    return render(request,"home.html",{"type":'h_user',"message":'user can login'})

#==============================USER LOGIN=========================================================
def loginform(request):
    un = request.POST.get['d_uname']
    pw = request.POST.get['d_pass']
    dbuser = register.objects.filter(email_id=un,password=pw)
    #print(dbuser)
    if not dbuser:
        return render(request,'home.html',{"type":'h_user',"message":'invalid'})
    else:
        return render(request,'home.html',{"type":'home'})

#===============================CONTACT US=========================================================


def feedback(request):
    u_Name = request.POST['u_name']
    u_email = request.POST['u_email']
    u_msg = request.POST['u_message']

    #print(u_name,u_cno,u_email,u_pass)

    fr = feedback(name=u_Name,email=u_email,msg=u_msg)
    fr.save()
    return render(request,"home.html",{"type":'home',"message":'thankyou '})


