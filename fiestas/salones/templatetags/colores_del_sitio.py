from django import template
from salones.models import parametros_colores, parametros_imagenes

register = template.Library()

@register.simple_tag
def get_color(nombre):
    color_resultado = parametros_colores.objects.filter(elemento=nombre).first()
    if not color_resultado:
        return "#AABVBCC"
    else:
        return color_resultado.color

@register.simple_tag
def get_imagen(nombre):
    imagen = parametros_imagenes.objects.filter(title=nombre).first()
    if not imagen:
        return f"No se encontro la imagen con el titulo {nombre}"
    else:
        return imagen