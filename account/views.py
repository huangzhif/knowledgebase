from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST) #获取post回来的数据
        if login_form.is_valid(): #如果post回来的数据是有效的
            cd = login_form.cleaned_data # 收集post回来的数据
            user = authenticate(username= cd['username'],password=cd['password']) #检验此用户是否为本网站项目的用户

            if user:
                login(request,user)
                return HttpResponse("welcome")
            else:
                return HttpResponse("sorry")

        else:
            return HttpResponse("invalid login")

    if request.method=="GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})


