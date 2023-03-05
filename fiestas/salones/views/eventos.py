from django.http import HttpResponse
from django.template import loader
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Sum
from django.template.loader import get_template
from xhtml2pdf import pisa
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

from .catalogos01 import *
from .eventos import *
from .personas import *
from .restview import * 
from .sistema import *

from salones.models import EncEvento, DetEvento
from salones.models import DesgloseServicio, ClasifServicio
from salones.forms import EventoCompletoForm, DetalleEventoForm




class eventos(ListView):
    model = EncEvento
    template_name = 'salones/evento/list_evento.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        datos = {
                'titulo': "Eventos",
                'add':"add_evento_completo",
                'add_label':'Nuevo evento',
                'update':'update_evento_completo',
                'borra':'borra_evento_completo',
                'detail':'detail_evento_completo',
                'encabezados': {
                    "folioevento":'ID',
                    "evento":"CLAVE EVENTO",
                    "persona":"CLIENTE", 
                    "opcion":"OPCION",
                    "nombre":"NOMBRE",
                    "banaprovada":"ACTIVA",
                    },
            }
        context.update(datos)
        return context



class add_evento_completo(LoginRequiredMixin, CreateView):
    model = EncEvento
    fields = ['cvetipoevento', 'cvepersona', 'nombre', 'numeropersonas', 'banaprovada']
    template_name = 'salones/catalogos/add.html'
    #success_url = reverse_lazy('update_evento_completo')
    
    def get_success_url(self):
        return reverse_lazy('update_evento_completo', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Evento"
        context['regresa'] = 'eventos'
        return context    


class update_evento_completo(LoginRequiredMixin, UpdateView):
    model = EncEvento
    #fields = ['cvetipoevento', 'cvepersona', 'nombre', 'numeropersonas', 'opcion', 'banaprovada',  ]
    template_name = 'salones/evento/update_evento.html'
    form_class = EventoCompletoForm
    #success_url = reverse_lazy('update_evento_completo')
    
    def get_success_url(self):
        return reverse_lazy('update_evento_completo', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        evento = super().get_object()
        detalles = DetEvento.objects.filter(cveevento=evento, opcion=evento.opcion)
        total = sum(filter(None, detalles.values_list('costo', flat=True)))
        context['titulo'] = "Actualiza Evento"
        context['regresa'] = 'eventos'
        context['detalles'] = detalles
        context['total'] = total
        return context   



# def detail_evento_completo(request, id_evento):    
#     evento = get_object_or_404(EncEvento, pk=EncEvento)
#     form = EventoCompletoForm(request.POST, instance=evento)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         return redirect(eventos)    
#     template = loader.get_template('salones/catalogos/add.html')
#     context = {'titulo': "Nuevo Evento", "form": form, 'regresa':'eventos'}
#     return HttpResponse(template.render(context, request))
    
class borra_evento_completo(DeleteView):
    model = EncEvento
    template_name = 'salones/catalogos/borrar.html'
    success_url = reverse_lazy('eventos')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borrar Evento"
        context['regresa'] = 'eventos'
        return context   


class detail_evento_completo(DetailView):
    model = EncEvento
    template_name = 'salones/evento/evento_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle del Evento"
        context['regresa'] = 'eventos'
        return context   



#######################################################################
###################### Detalle del evento #############################

class add_evento_detalle(LoginRequiredMixin, CreateView):
    model = DetEvento
    template_name = 'salones/evento/detalle_evento_form.html'          
    form_class = DetalleEventoForm

    def get_form(self):
        form = super().get_form()
        form.fields['fecha'].widget = DateTimePickerInput()
        return form


    def form_valid(self, form):
        form.save(commit=False)
        evento =  EncEvento.objects.get(pk=self.kwargs['pk'])
        form.instance.cveevento = evento
        form.instance.opcion = evento.opcion
        form.save()
        return super(add_evento_detalle, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('update_evento_completo', kwargs={'pk': self.object.cveevento.id_pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Nuevo Detalle"
        context['regresa'] = f"eventos"
        return context    


class update_evento_detalle(LoginRequiredMixin, UpdateView):
    model = DetEvento    
    template_name = 'salones/evento/detalle_evento_form.html'          
    form_class = DetalleEventoForm
 
    def get_success_url(self):
        return reverse_lazy('update_evento_completo', kwargs={'pk': self.object.cveevento.id_pk})


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Actualiza Detalle del Evento"
        context['regresa'] = f"eventos"
        return context

class borra_evento_detalle(LoginRequiredMixin, DeleteView):
    model = DetEvento
    template_name = 'salones/catalogos/borrar.html'
    
    def get_success_url(self):
        return reverse_lazy('update_evento_completo', kwargs={'pk': self.object.cveevento.id_pk})

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Borra Detalle de Evento"
        context['regresa'] = f"eventos"
        return context

class detail_evento_detalle(LoginRequiredMixin, DetailView):
    model = DetEvento
    template_name = 'salones/evento/detalle_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Especificacion del detalle del evento"
        context['regresa'] = f"eventos"
        return context
    
########################################################################
########################### DropDowns ############################
########################################################################

def load_clases_servicio(request):
    id_tipo_servicio = request.GET.get('clasificacion')
    clasificacion_servicio = ClasifServicio.objects.filter(cvetiposervicio=id_tipo_servicio).order_by('descripcion')
    return render(request, 'salones/evento/drowdown.html', {'lista': clasificacion_servicio})


def load_desglose_servicio(request):
    id_tipo_servicio = request.GET.get('desglose')
    desglose_servicio = DesgloseServicio.objects.filter(cveclasifservicio=id_tipo_servicio).order_by('descripcion')
    return render(request, 'salones/evento/drowdown.html', {'lista': desglose_servicio})


########################################################################
###########################   Reporte PDF   ############################
########################################################################

@login_required
def generate_pdf(request, pk):
    # # Define the data for the PDF
    evento = EncEvento.objects.filter(id_pk = pk).first()
    detalles = DetEvento.objects.filter(cveevento = pk, opcion=evento.opcion)
    total = sum(filter(None, detalles.values_list('costo', flat=True)))

    # Define the title for the PDF
    title = evento

    # Get the template
    template = get_template('salones/evento/reporte.html')

    # Render the template with the data
    html = template.render({'evento': title, 'detalle': detalles, 'total': total})

    # Create a new PDF object
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="user_info.pdf"'

    # Generate the PDF
    pisa.CreatePDF(html, dest=response)

    return response