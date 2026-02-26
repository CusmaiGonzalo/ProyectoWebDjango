from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'ProyectoWebApp/home.html')

def Servicios(request):
    return render(request, 'ProyectoWebApp/servicios.html')

def Tienda(request):
    return render(request, 'ProyectoWebApp/tienda.html')

def Blog(request):
    return render(request, 'ProyectoWebApp/blog.html')

def Contacto(request):
    return render(request, 'ProyectoWebApp/contacto.html')