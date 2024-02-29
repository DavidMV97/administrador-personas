from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona

# Create your views here.
def bienvenido(request):
    num_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request,'home.html', {'num_personas': num_personas, 'personas': personas})



