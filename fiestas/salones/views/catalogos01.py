from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import loader
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from .catalogos01 import *
from .catalogos02 import *
from .eventos import *
from .personas import *
from .restview import * 
from .sistema import *

from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio,
    TipoPersona, 
)
from salones.forms import (
    ActividadForm, 
    EventoForm, 
    ServicioForm,
    TipoClienteForm,
)

################################################
##########   Tipo Actividad   ##################

def add_actividad(request):
    form = ActividadForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_actividad)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nueva Actividad", "form": form, 'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

def update_actividad(request, id_actividad):
    actividad = get_object_or_404(TipoActividad, pk=id_actividad)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=actividad)
        if form.is_valid():
            form.save()
            return redirect(lista_actividad)
    else:
        form = EventoForm(instance=actividad)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': actividad, 'titulo': "Actualiza Actividad", "form": form, 'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

class detalle_actividad(DetailView):
    model = TipoActividad
    template_name = 'salones/catalogos/detalle.html' 
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Actividad"
        context['regresa'] = 'lista_actividad'
        return context   

class borra_actividad(DeleteView):
    model = TipoActividad
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('lista_actividad')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Actividad"
        context['regresa'] = 'lista_actividad'
        return context   

def lista_actividad(request):
    actividad_list = TipoActividad.objects.all().order_by('descripcion').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': actividad_list,
        'titulo': "Actividades",
        'add':"add_actividad",
        'add_label':'Nueva actividad',
        'update':'update_actividad',
        'detalle':'detalle_actividad',
        'borra':'borra_actividad',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))

################################################
############   Tipo Evento   ##################
  

def add_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect(lista_evento)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'lista_evento'}
    return HttpResponse(template.render(context, request))

class update_evento(UpdateView):
    model = TipoEvento
    fields = ['clave','descripcion','bandactivo']
    success_url = reverse_lazy('lista_evento')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Evento"
        context['regresa'] = 'lista_evento'
        return context

class detalle_evento(DetailView):
    model = TipoEvento
    template_name = 'salones/catalogos/detalle.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Tipo de Evento"
        context['regresa'] = 'lista_evento'
        return context 


class borra_tipo_evento(DeleteView):
    model = TipoEvento
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('lista_evento')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Tipo de Evento"
        context['regresa'] = 'lista_evento'
        return context 


class lista_evento(ListView):
    model = TipoEvento
    template_name = ('salones/catalogos/list.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista'] = TipoEvento.objects.all().order_by('clave').values()
        datos = {
            'titulo': "Eventos",
            'add':"add_evento",
            'add_label':'Nuevo Evento',
            'update':'update_evento',        
            'detalle':'detalle_evento',     
            'borra':'borra_evento',
            'encabezados': {"id":'Folio',"clav e":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    
################################################
###########   Tipo Servicio   ##################

def add_servicio(request):
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(lista_servicio)    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Servicio", "form": form, 'regresa':'lista_servicio'}
    return HttpResponse(template.render(context, request))   

def update_servicio(request, id_servicio):
    servicio = get_object_or_404(TipoServicio, pk=id_servicio)
    if request.method == 'POST':
        form = EventoForm(request.POST,instance=servicio)
        if form.is_valid():
            form.save()
            return redirect(lista_servicio)
    else:
        form = ServicioForm(instance=servicio)
    template = loader.get_template('salones/catalogos/update.html')
    context = {'catalogo': servicio, 'titulo': "Actualiza Servicio", "form": form, 'regresa':'lista_servicio'}
    return HttpResponse(template.render(context, request))

class borra_servicio(DeleteView):
    model = TipoServicio
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('lista_servicio')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Servicio"
        context['regresa'] = 'lista_servicio'
        return context   

class detalle_servicio(DetailView):
    model = TipoServicio
    template_name = 'salones/catalogos/detalle.html'    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Servicio"
        context['regresa'] = 'lista_servicio'
        return context  

def lista_servicio(request):
    servicio_list = TipoServicio.objects.all().order_by('clave').values()
    template = loader.get_template('salones/catalogos/list.html')
    context = {
        'lista': servicio_list,
        'titulo': "Servicios",
        'add':"add_servicio",
        'add_label':'Nuevo Servicio',
        'update':'update_servicio',
        'detalle':'detalle_servicio',
        'borra':'detalle_servicio',
        'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
    }
    return HttpResponse(template.render(context, request))

################################################
##########   Tipo Persona #####################

class lista_tipo_persona(ListView):
    model = TipoPersona
    template_name  = 'salones/catalogos/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        lista = TipoPersona.objects.all().order_by('clave').values()
        datos = {
            'lista': lista,
            'titulo': "Tipo Persona",
            'add':"add_tipo_cliente",
            'add_label':'Nuevo Tipo Persona',
            'update':'update_tipo_cliente',  
            'detalle':'detalle_tipo_persona',
            'borra':'borra_tipo_persona',
            'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    

def add_tipo_cliente(request):
    form = TipoClienteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save() 
        return redirect('lista_tipo_cliente')    
    template = loader.get_template('salones/catalogos/add.html')
    context = {'titulo': "Nuevo Tipo Cliente", "form": form, 'regresa':'lista_tipo_cliente'}
    return HttpResponse(template.render(context, request))

def update_tipo_cliente(request, id_tipo_persona):
    tipo_persona = get_object_or_404(TipoPersona, pk=id_tipo_persona)
    if request.method == 'POST':
        form = TipoClienteForm(request.POST,instance=tipo_persona)
        if form.is_valid():
            form.save()
            return redirect('lista_tipo_cliente')
    else:
        form = TipoClienteForm(instance=tipo_persona)  
    template = loader.get_template('salones/catalogos/update.html')
    context = {"catalogo": tipo_persona, 'titulo': "Actualiza Tipo Cliente", "form": form, 'regresa':'lista_tipo_cliente'}
    return HttpResponse(template.render(context, request))


class detalle_tipo_persona(DetailView):
    model = TipoPersona
    template_name = 'salones/catalogos/detalle.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Tipo de Persona"
        context['regresa'] = 'lista_tipo_cliente'
        return context 


class borra_tipo_persona(DeleteView):
    model = TipoPersona
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('lista_tipo_cliente')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Tipo de Persona"
        context['regresa'] = 'lista_tipo_cliente'
        return context 