from django.http import HttpResponse
from django.shortcuts import render

#recibe tres argumentos, el primero es a peticion, el segundo el nombre de nuestro archivo html, el ultimo es cun diccionario de clave valor
def saludo(request):
    return render(request,"index.html",{
        'titulo': 'Personas',
        'mensaje':'Ingreso',
        'personas':[
            {'titulo':'Maria','edad':15,'adulto':False},
            {'titulo':'Matias','edad':18,'adulto':True},
            {'titulo':'Jorge','edad':11,'adulto':False},
            {'titulo':'Marta','edad':44,'adulto':True}
        ]
    })