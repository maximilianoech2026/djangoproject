from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Proyecto  # Importamos el modelo Proyecto

# Vista de inicio, requiere login
@login_required(login_url='login')  # Solo usuarios logueados pueden ver esta página
def inicio(request):
    proyectos = Proyecto.objects.all()  # Trae todos los proyectos desde la DB
    return render(request, 'proyectos/home.html', {'proyectos': proyectos})

# Vista que muestra la lista completa de proyectos (opcional, también puede requerir login)
@login_required(login_url='login')
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})
