from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select, CheckboxInput
from salones.models import (
    TipoActividad, 
    TipoEvento, 
    TipoServicio, ClasifServicio, DesgloseServicio,
    TipoPersona, 
    EncEvento, 
    DetEvento,
    PersonaPrincipal)

class ActividadForm(ModelForm):
    class Meta:
        model = TipoActividad
        fields = '__all__'

class EventoForm(ModelForm):
    class Meta:
        model = TipoEvento
        #fields = ('cvetipoevento', 'desctipoevento', 'bandactivo')
        fields = '__all__'

class ServicioForm(ModelForm):
    class Meta:
        model = TipoServicio
        fields = '__all__'


class EventoCompletoForm(ModelForm):
    class Meta:
        model = EncEvento
        fields = ['cvetipoevento', 'cvepersona', 'nombre', 
                  'numeropersonas', 'opcion', 'banaprovada',  
                  ]
        widgets = {
            'cvetipoevento': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                }),
            'cvepersona': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                }),
            'nombre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border-radius: 3rem;',
                'placeholder': 'nombre'
                }),
            'numeropersonas': NumberInput(attrs={
                'class': "form-control disable", 
                'style': 'max-width: 300px; border-radius: 3rem;',
                'placeholder': 'numero de personas'
                }),
            'opcion': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 50px; border-radius: 3rem;',
                }),
            'banaprovada': CheckboxInput(attrs={
                'class': "form-control",
                }),

        }


class DetalleEventoForm(ModelForm):
    class Meta:
        model = DetEvento
        fields = ['cvetipoactividad','cvetiposervicio',
        'cveclasifservicio','cvedesgloseservicio', 'precio','costo', 'proveedor',
        'fecha','tiempo','estatus','nota', 
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cveclasifservicio'].queryset = ClasifServicio.objects.none()
        self.fields['cvedesgloseservicio'].queryset = DesgloseServicio.objects.none()
        self.fields['cvedesgloseservicio'].required = False
        self.fields['proveedor'].queryset = PersonaPrincipal.objects.filter(cvetipopersona=3).all()

        if 'cvetiposervicio' in self.data:
            try:
                servicio_id = int(self.data.get('cvetiposervicio'))
                self.fields['cveclasifservicio'].queryset = ClasifServicio.objects.filter(cvetiposervicio=servicio_id).order_by('descripcion')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['cveclasifservicio'].queryset = ClasifServicio.objects.filter(cvetiposervicio=self.instance.cvetiposervicio.pk).order_by('descripcion')

        if 'cveclasifservicio' in self.data:
            try:
                clasificacion_id = int(self.data.get('cveclasifservicio'))
                self.fields['cvedesgloseservicio'].queryset = DesgloseServicio.objects.filter(cveclasifservicio=clasificacion_id).order_by('descripcion')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['cvedesgloseservicio'].queryset = DesgloseServicio.objects.filter(cveclasifservicio=self.instance.cveclasifservicio.pk).order_by('descripcion')


class TipoClienteForm(ModelForm):
    class Meta:
        model = TipoPersona
        fields = '__all__'


class PersonaPrincipalForm(ModelForm):
    class Meta:
        model = PersonaPrincipal
        fields = '__all__'

