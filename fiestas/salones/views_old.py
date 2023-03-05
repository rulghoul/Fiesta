from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio,
    TipoPersona, 
    Foto, 
    EncEvento,
    PersonaPrincipal,
)
from .forms import (
    ActividadForm, 
    EventoForm, 
    ServicioForm,
    EventoCompletoForm,
    PersonaPrincipalForm,
    TipoClienteForm,
    )


#Catalogos

