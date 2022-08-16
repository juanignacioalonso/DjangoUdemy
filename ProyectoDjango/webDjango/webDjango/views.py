from django.http import HttpResponse

def Saludo(recuest):
    return HttpResponse("Hola como estas")