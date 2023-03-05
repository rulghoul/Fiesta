# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True44
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from simple_history.models import HistoricalRecords
from colorfield.fields import ColorField

class ClasifServicio(models.Model):
    idclasifservicio = models.SmallAutoField(db_column='IdClasifServicio', primary_key=True)  
    cvetiposervicio = models.ForeignKey('TipoServicio', models.CASCADE, db_column='CveTipoServicio')  
    cveclasifservicio = models.CharField(db_column='CveClasifServicio', unique=False, max_length=20)  
    descripcion = models.CharField(db_column='DescClasifServicio', unique=False, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'clasif_servicio'


class DesgloseServicio(models.Model):
    iddesgloseservicio = models.SmallAutoField(db_column='IdDesgloseServicio', primary_key=True)  
    cveclasifservicio = models.ForeignKey(ClasifServicio, models.CASCADE, db_column='CveClasifServicio')  
    cvedesgloseservicio = models.CharField(db_column='CveDesgloseServicio', unique=False, max_length=20)  
    descripcion = models.CharField(db_column='DescDesgloseServicio', unique=False, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  
    datelastupdate = models.DateTimeField(db_column='DateLastUpdate')  
    
    def __str__(self) -> str:
        return self.descripcion
    
    class Meta:
        db_table = 'desglose_servicio'



class EstatusActividad(models.Model):
    idestatusactividad = models.SmallAutoField(db_column='IdEstatusActividad', primary_key=True)  
    clave = models.CharField(db_column='CveEstatusActividad', unique=True, max_length=20)  
    descripcion = models.CharField(db_column='DescEstatusActividad', unique=True, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'estatus_actividad'


class FasesProcesos(models.Model):
    idfase = models.SmallAutoField(db_column='IdFase', primary_key=True)  
    #cveproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='CveProceso')  
    cvefase = models.CharField(db_column='CveFase', unique=True, max_length=20)  
    descfase = models.CharField(db_column='DescFase', unique=True, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    class Meta:
        db_table = 'fases_procesos'




class TipoPersona(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoPersona', primary_key=True)  
    clave = models.CharField(db_column='CveTipoPersona', unique=True, max_length=20, verbose_name='Clave')  
    descripcion = models.CharField(db_column='DescTipoPersona', unique=True, max_length=50, verbose_name='Descripcion')  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_PERSONA'



class PersonaPrincipal(models.Model):
    idpersonaprincipal = models.SmallAutoField(db_column='IdPersonaPrincipal', primary_key=True)  
    cvetipopersona = models.ForeignKey(TipoPersona, models.DO_NOTHING, db_column='CveTipoPersona')  
    nombre = models.CharField(db_column='Nombre', max_length=100)  
    primer_apellido = models.CharField(db_column='Primer_Apellido', max_length=50, blank=True, null=True)  
    segundo_apellido = models.CharField(db_column='Segundo_Apellido', max_length=50, blank=True, null=True)  
    correo = models.EmailField(db_column='Correo', max_length=70)  
    telefono1 = models.CharField(db_column='Telefono1', max_length=50)  
    telefono2 = models.CharField(db_column='Telefono2', max_length=50, blank=True, null=True)  
    datestar = models.DateTimeField(db_column='DateStar',auto_now_add=True)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return f"{self.nombre} {(self.primer_apellido or '')} {(self.segundo_apellido or '')}"

    class Meta:
        db_table = 'persona_principal'


class Procesos(models.Model):
    id_pk = models.SmallAutoField(db_column='IdProceso', primary_key=True)  
    clave = models.CharField(db_column='CveProceso', unique=True, max_length=20)  
    descripcion = models.CharField(db_column='DescProceso', unique=True, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.clave

    class Meta:
        db_table = 'procesos'


class SeguimientoEvento(models.Model):
    folioevento = models.PositiveSmallIntegerField(db_column='FolioEvento', primary_key=True)  
    cvetipopersona = models.CharField(db_column='CveTipoPersona', max_length=20)  
    cvepersona = models.CharField(db_column='CvePersona', max_length=20)  
    cvetipoevento = models.CharField(db_column='CveTipoEvento', max_length=20)  
    cveproceso = models.CharField(db_column='CveProceso', max_length=20)  
    cvefase = models.CharField(db_column='CveFase', max_length=20)  
    history = HistoricalRecords()

    class Meta:
        db_table = 'SEGUIMIENTO_EVENTO'


class TipoActividad(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoActividad', primary_key=True)  
    clave = models.CharField(db_column='CveTipoActividad', max_length=20,)  
    descripcion = models.CharField(db_column='DescTipoActividad', max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_ACTIVIDAD'


class TipoEvento(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoEvento', primary_key=True)  
    clave = models.CharField(db_column='CveTipoEvento', unique=True, max_length=20)  
    descripcion = models.CharField(db_column='DescTipoEvento', unique=False, max_length=50)  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_EVENTO'


class TipoServicio(models.Model):
    id_pk = models.SmallAutoField(db_column='IdTipoServicio', primary_key=True)  
    clave = models.CharField(db_column='CveTipoServicio', unique=True, max_length=20, verbose_name='Clave')  
    descripcion = models.CharField(db_column='DescServicio', max_length=50, verbose_name='Descripcion')  
    bandactivo = models.BooleanField(db_column='BandActivo', blank=False, null=False, default=True, verbose_name='Activo')  

    def __str__(self) -> str:
        return self.descripcion

    class Meta:
        db_table = 'TIPO_SERVICIO'


class Foto(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Foto'


class EncEvento(models.Model):
    id_pk = models.SmallAutoField(db_column='FolioEvento', primary_key=True)  
    cvetipoevento = models.ForeignKey(TipoEvento, models.DO_NOTHING, db_column='CveTipoEvento', verbose_name="Tipo de evento",)  
    cvepersona = models.ForeignKey(PersonaPrincipal, models.DO_NOTHING, db_column='CvePersona', verbose_name="Persona")  
    opcion = models.PositiveSmallIntegerField(db_column='Opcion', null=False, default=1, choices=[(1,'1'),(2,'2'),(3,'3')], verbose_name="Opcion")  
    nombre = models.CharField(db_column='Nombre', max_length=50, blank=True, null=True)  
    numeropersonas = models.PositiveSmallIntegerField(db_column='numero_personas',default=0,  blank=False, null=True, verbose_name="Numero de personas")  
    banaprovada = models.BooleanField(db_column='BanAprovada', blank=False, null=False, default=True, verbose_name='Aprobada')  
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre} para el cliente {self.cvepersona} del tipo {self.cvetipoevento}"

    class Meta:
        db_table = 'enc_evento'


class DetEvento(models.Model):
    iddetalle = models.SmallAutoField(db_column='IdDetalle', primary_key=True)  
    cveevento = models.ForeignKey('EncEvento', models.CASCADE, db_column='CveEvento', default=None, null=True, )  
    opcion = models.PositiveSmallIntegerField(db_column='Opcion', null=False, default=1, choices=[(1,'1'),(2,'2'),(3,'3')], verbose_name="Opcion")
    cvetipoactividad = models.ForeignKey('TipoActividad', models.DO_NOTHING, db_column='CveTipoActividad', verbose_name='Actividad')  
    proveedor = models.ForeignKey('PersonaPrincipal', models.DO_NOTHING, null=True, default=None, db_column='cveproveedor', verbose_name='Proveedor')  
    cvedesgloseservicio = models.ForeignKey('DesgloseServicio', models.DO_NOTHING, null=True, default=None, db_column='CveDesgloseServicio', verbose_name='Desglose')  
    cveclasifservicio = models.ForeignKey('ClasifServicio', models.DO_NOTHING, db_column='CveClasifServicio', verbose_name='Clasificacion')  
    cvetiposervicio = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='CveTipoServicio', verbose_name='Servicio')  
    costo = models.FloatField(db_column='Costo', blank=True, null=True, verbose_name='Costo')  
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True, verbose_name='Fecha')  
    tiempo = models.PositiveSmallIntegerField(db_column='Tiempo', null=True, blank=False, default=None,  verbose_name='Tiempo')
    estatus = models.ForeignKey(EstatusActividad, models.DO_NOTHING, db_column='CveEstatus', null=True, default=None, verbose_name='Estatus')
    nota = models.CharField(db_column='Notas', null= True, blank=True, default=None, max_length=100,  verbose_name='Notas')
    history = HistoricalRecords()

    class Meta:
        db_table = 'det_evento'



class Egresos(models.Model):
    id_egresos = models.SmallAutoField(primary_key=True)
    cve_detalle = models.ForeignKey(DetEvento, models.DO_NOTHING, db_column='Cve_detalle')  
    monto = models.FloatField(db_column='Monto')  
    spei = models.CharField(db_column='SPEI', max_length=50)  
    history = HistoricalRecords()

    class Meta:
        db_table = 'egresos'

class Ingresos(models.Model):
    idingresos = models.OneToOneField(EncEvento, models.DO_NOTHING, db_column='IdIngresos', primary_key=True)  
    cveevento = models.PositiveSmallIntegerField(db_column='CveEvento')  
    monto = models.FloatField(db_column='Monto')  
    spei = models.CharField(db_column='SPEI', max_length=50, blank=True, null=True)  
    history = HistoricalRecords()

    class Meta:
        db_table = 'ingresos'


class parametros_colores(models.Model):
    elemento = models.CharField(db_column='elemento', max_length=50, blank=False, null=False)
    color = ColorField(default='#FF0000')

    class Meta:
        db_table = 'parametros_colores'

class parametros_imagenes(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title