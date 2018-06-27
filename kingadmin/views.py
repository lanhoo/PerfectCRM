from django.shortcuts import render, redirect
from kingadmin import setup_app
from django.contrib.auth import authenticate, login, logout
from kingadmin.sites import site

setup_app.kingadmin_auto_discover()

# print('sites:', site.enable_admin)

def index(request):

    return render(request, 'kingadmin/app_index.html', {'site':site})


def acc_login(request):
    error_msg = ''

    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('password')
        user = authenticate(username=name, password=pwd)
        if user:
            login(request, user)
            print(request.POST.get('next'))
            print(request.POST.get('next'))
            return redirect(request.GET.get('next', '/'))
        else:
            error_msg = 'Wrong password or username!'

    return render(request, 'login.html', {'error_msg': error_msg})


def acc_logout(request):
    logout(request)
    return redirect('login')
