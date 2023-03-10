from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .catalogos01 import *
from .eventos import *
from .personas import *
from .restview import * 
from .sistema import *

from salones.models import parametros_colores, parametros_imagenes

def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'salones/account.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'salones/login.html', {'error_message': 'Nombre o contraseña incorrecta.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'salones/login.html')

def home_view(request):   
    template = loader.get_template('home.html')
    colores = parametros_colores.objects.all().order_by('elemento').values()
    #graficos = parametros_imagenes.objects.all().order_by('descripcion').values()
    context = {'titulo': "Nueva Actividad", 
               'colores': colores, 
               'imagenes': [], 
               'regresa':'lista_actividad'}
    return HttpResponse(template.render(context, request))

def base_view(request):
    colores = parametros_colores.objects.all().order_by('elemento').values()
    return render(request, 'base.html', {'site_colors': colores})
