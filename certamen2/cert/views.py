from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proyecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

@login_required
def nuevo_proyecto(request):
    if(request.POST):
    
        nombre = request.POST["txtNombre"]
        tema = request.POST['txtTema']

        proyecto = Proyecto()
        proyecto.nombre = nombre
        proyecto.tema = tema
        proyecto.estudiante = request.user
        
        proyecto.save()
        return redirect("index")
        
    return render(request, 'formulario.html')

def index(request):
    
    estalogueado = request.user.is_authenticated
    data = {}
    
    filtro = request.GET.get('filtro')
    if filtro == 'on':
        proyectos = Proyecto.objects.filter(profesor_patrocinador__isnull=True)
    else:
        proyectos = Proyecto.objects.all()
    
    data["proyectos"] = proyectos
    data["estalogueado"] = estalogueado

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    return render(request, "index.html", data)









