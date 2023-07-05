from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request): 
    return render(request, "core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def carta(request):
    return render(request, "core/carta.html")

def sucursales(request):
    return render(request, "core/sucursales.html")