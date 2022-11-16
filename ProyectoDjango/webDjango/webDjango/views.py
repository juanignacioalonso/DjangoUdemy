from django.http import HttpResponse
from django.shortcuts import render

#recibe tres argumentos, el primero es a peticion, el segundo el nombre de nuestro archivo html, el ultimo es cun diccionario de clave valor
def saludo(request):
    return render(request,"index.html",{
        'mensaje':'Este es un mensaje de mi función'
    })