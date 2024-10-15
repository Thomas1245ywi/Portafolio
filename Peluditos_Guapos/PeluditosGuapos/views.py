from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm



def index(request):
    return render(request, 'index.html')


def index_real(request):
    return render(request, 'index_real.html')



def registrarme(request):
    #Revisa si los campos estan llenos
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        user = form.save()


        if user:
            login(request,user)
            return redirect('index_real')
        


        


    return render(request, 'registrarme.html',{
        'form': form

    })




def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)


        if user:

            login(request, user)
            return redirect('index_real')

        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'inicio_sesion.html',{

    })


#reques poseee la ssesion y django nos brinda el metodo logut para cerrar sesion
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('inicio_sesion')
