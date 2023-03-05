from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import TipoActividad, TipoEvento, TipoServicio, Foto, EncEvento

admin.site.register(TipoActividad)
admin.site.register(TipoEvento)
admin.site.register(TipoServicio)
admin.site.register(Foto)

admin.site.register(EncEvento, SimpleHistoryAdmin)