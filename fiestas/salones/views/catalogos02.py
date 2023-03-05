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

from salones.models import DesgloseServicio, ClasifServicio, parametros_colores, parametros_imagenes

####### Clasificacion Servicio #########

class desglose_servicio_lista(ListView):
    model = ClasifServicio
    template_name  = 'salones/catalogos/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        lista = TipoPersona.objects.all().order_by('clave').values()
        datos = {
            'lista': lista,
            'titulo': "Desglose de Servicio",
            'add':"add_desglose_servicio",
            'add_label':'Nuevo desglose de servicio',
            'update':'update_desglose_servicio',  
            'detalle':'detalle_desglose_servicio',
            'borra':'borra_desglose_servicio',
            'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    



####### Desglose Servicio #########

class desglose_servicio_lista(ListView):
    model = DesgloseServicio
    template_name  = 'salones/catalogos/list.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        lista = TipoPersona.objects.all().order_by('clave').values()
        datos = {
            'lista': lista,
            'titulo': "Desglose de Servicio",
            'add':"add_desglose_servicio",
            'add_label':'Nuevo desglose de servicio',
            'update':'update_desglose_servicio',  
            'detalle':'detalle_desglose_servicio',
            'borra':'borra_desglose_servicio',
            'encabezados': {"id":'ID',"clave":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    


####### Parametros de colores #########


class add_color(CreateView):
    model = parametros_colores
    success_url = reverse_lazy('list_color')
    fields = ['elemento', 'color']
    template_name = 'salones/catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Color"
        context['regresa'] = 'list_color'
        return context

class update_color(UpdateView):
    model = parametros_colores
    fields = ['elemento', 'color']
    success_url = reverse_lazy('list_color')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Color"
        context['regresa'] = 'list_color'
        return context


class list_color(ListView):
    model = parametros_colores
    template_name = ('salones/parametros/listColor.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Colores",
            'add':"add_color",
            'add_label':'Nuevo color',
            'update':'update_color',    
            'encabezados': {"elemento":'Elemento',"color":"Color"},
        }
        context.update(datos)
        return context
    


####### Parametros de imagenes #########


class add_parametro_imagen(CreateView):
    model = parametros_imagenes
    success_url = reverse_lazy('list_color')
    fields = ['elemento', 'color']
    template_name = 'salones/catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Color"
        context['regresa'] = 'list_color'
        return context

class update_parametro_imagen(UpdateView):
    model = parametros_imagenes
    fields = ['elemento', 'color']
    success_url = reverse_lazy('list_color')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Color"
        context['regresa'] = 'list_color'
        return context


class list_parametro_imagen(ListView):
    model = parametros_imagenes
    template_name = ('salones/parametros/listColor.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Colores",
            'add':"add_color",
            'add_label':'Nuevo color',
            'update':'update_color',    
            'encabezados': {"elemento":'Elemento',"color":"Color"},
        }
        context.update(datos)
        return context
    


