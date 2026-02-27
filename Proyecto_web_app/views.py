from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.

def Home(request):
    return render(request, 'ProyectoWebApp/home.html')

def Servicios(request):

    servicios = Servicio.objects.all()
    return render(request, 'ProyectoWebApp/servicios.html', {'servicios': servicios})

def Tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')

def Blog(request):
    return render(request, 'ProyectoWebApp/blog.html')

def Contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html')