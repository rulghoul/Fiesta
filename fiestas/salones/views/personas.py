from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .catalogos01 import *
from .eventos import *
from .personas import *
from .restview import * 
from .sistema import *

from salones.models import PersonaPrincipal
from salones.forms import PersonaPrincipalForm

class personas(ListView):
    model = PersonaPrincipal
    template_name  = 'salones/personas/list_cliente.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['lista'] = EncEvento.objects.all()

        datos = {
            'titulo': "Personas",
            'add':"add_cliente",
            'add_label':'Nueva Persona',
            'update':'update_cliente',
            'detalle':'detalle_cliente',
            'borra':'borra_cliente',
            'encabezados': {
                "id":"ID",
                "nombre":'NOMBRE',
                "primer_apellido":"PRIMER APELLIDO",
                "segundo_apellido":"SEGUNDO APELLIDO", 
                "cvetipopersona":"TIPO",
                "correo":"CORREO",
                },
        }
        context.update(datos)
        return context


def add_cliente(request):
    form = PersonaPrincipalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('clientes')    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nueva Persona", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   

def update_cliente(request, id_persona):
    persona = get_object_or_404(PersonaPrincipal, pk=id_persona)
    if request.method == 'POST':
        form = PersonaPrincipalForm(request.POST,instance=persona)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = PersonaPrincipalForm(instance=persona)  
    template = loader.get_template('salones/catalogos/update.html')
    context = {"catalogo": persona,'titulo': "Actualiza persona", "form": form, 'regresa':'clientes'}
    return HttpResponse(template.render(context, request))   



class detalle_persona(DetailView):
    model = PersonaPrincipal
    template_name = 'salones/personas/detalle_persona.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Persona"
        context['regresa'] = 'clientes'
        return context 


class borra_persona(DeleteView):
    model = PersonaPrincipal
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('clientes')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Persona"
        context['regresa'] = 'clientes'
        return context 