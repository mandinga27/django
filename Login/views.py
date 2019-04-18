from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def login(request):
    #aca se recibe lo que fue enviado en datos de login.html
    if request.POST:
        print("ESTOY RECIBIENDO UN POST")
        print(request.POST)
        #HttpResponseRedirect(reverse('login_login' redirige la pagina al momento de ingresar nuevo usuario al
        #apretar F5
        return HttpResponseRedirect(reverse('login_login'))
    return render(request, 'login.html', {})


def logout(request):
    print("HOLA")
    return render(request, 'logout.html', {})
