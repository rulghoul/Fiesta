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

class clasificacion_servicio_lista(ListView):
    model = ClasifServicio
    template_name  = 'salones/catalogos/listClasificacion.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Clasificacion de Servicio",
            'add':"add_clasificacion_servicio",
            'add_label':'Nueva clasificacion de servicio',
            'update':'update_clasificacion_servicio',  
            'detalle':'detalle_clasificacion_servicio',
            'borra':'borra_clasificacion_servicio',
            'encabezados': {"cvetiposervicio":'TIPO SERVICIO',"cveclasifservicio":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context
    

class add_clasificacion_servicio(CreateView):
    model = ClasifServicio
    success_url = reverse_lazy('clasificacion_servicio_lista')
    fields = ['cvetiposervicio', 'cveclasifservicio', 'descripcion', 'bandactivo']
    template_name = 'salones/catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Color"
        context['regresa'] = 'clasificacion_servicio_lista'
        return context

class update_clasificacion_servicio(UpdateView):
    model = ClasifServicio
    fields = ['cvetiposervicio', 'cveclasifservicio', 'descripcion', 'bandactivo']
    success_url = reverse_lazy('clasificacion_servicio_lista')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Clasificacion de Servicio"
        context['regresa'] = 'clasificacion_servicio_lista'
        return context
    
class borra_clasificacion_servicio(DeleteView):
    model = ClasifServicio
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('clasificacion_servicio_lista')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Clasificacion Servicio"
        context['regresa'] = 'clasificacion_servicio_lista'
        return context   


####### Desglose Servicio #########

class desglose_servicio_lista(ListView):
    model = DesgloseServicio
    template_name  = 'salones/catalogos/listDesglose.html'
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
            'encabezados': {"cveclasifservicio":'TIPO CLASIFICACION',"cvedesgloseservicio":"CLAVE","descripcion":"DESCRIPCION", "activo":"ACTIVO"},
        }
        context.update(datos)
        return context

class add_desglose_servicio(CreateView):
    model = DesgloseServicio
    success_url = reverse_lazy('desglose_servicio_lista')
    fields = ['cveclasifservicio', 'cvedesgloseservicio', 'descripcion', 'bandactivo']
    template_name = 'salones/catalogos/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Desglose servicio"
        context['regresa'] = 'desglose_servicio_lista'
        return context

class update_desglose_servicio(UpdateView):
    model = DesgloseServicio
    fields = ['elemento', 'color']
    success_url = reverse_lazy('desglose_servicio_lista')
    template_name = 'salones/catalogos/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Desglose Servicio"
        context['regresa'] = 'desglose_servicio_lista'
        return context
    
class borra_desglose_servicio(DeleteView):
    model = DesgloseServicio
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('desglose_servicio_lista')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Desglose Servicio"
        context['regresa'] = 'desglose_servicio_lista'
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


class add_imagen(CreateView):
    model = parametros_imagenes
    success_url = reverse_lazy('list_imagenes')
    fields = ['title', 'image',]
    template_name = 'salones/parametros/add.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nueva Imagen"
        context['regresa'] = 'list_imagenes'
        return context

class update_imagen(UpdateView):
    model = parametros_imagenes
    fields = ['title', 'image',]
    success_url = reverse_lazy('list_imagenes')
    template_name = 'salones/parametros/update.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Imagen"
        context['regresa'] = 'list_imagen'
        return context


class list_imagen(ListView):
    model = parametros_imagenes
    template_name = ('salones/parametros/listImagenes.html')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        datos = {
            'titulo': "Parametros Imagenes",
            'add':"add_imagen",
            'add_label':'Nueva imagen',
            'update':'update_imagen',    
            'encabezados': {"title":'Nombre',"image":"Imagen"},
        }
        context.update(datos)
        return context
    


