from django import template
from salones.models import parametros_colores

register = template.Library()

@register.simple_tag
def get_color(nombre):
    color_resultado = parametros_colores.objects.filter(elemento=nombre).first()
    if not color_resultado:
        return "#AABVBCC"
    else:
        return color_resultado.color


