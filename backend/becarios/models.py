# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BecalImportado(models.Model):
    cod_postulacion = models.CharField(
        db_column='COD_POSTULACION',
        max_length=60,
        primary_key=True  # 👈 usamos este campo como clave primaria
    )
    condicion = models.CharField(db_column='CONDICION', max_length=60, blank=True, null=True)
    condicion_contractual = models.CharField(db_column='CONDICION_CONTRACTUAL', max_length=60, blank=True, null=True)
    nombres = models.CharField(db_column='NOMBRES', max_length=60, blank=True, null=True)
    apellidos = models.CharField(db_column='APELLIDOS', max_length=60, blank=True, null=True)
    sexo = models.CharField(db_column='SEXO', max_length=60, blank=True, null=True)
    departamento_residencia = models.CharField(db_column='DEPARTAMENTO_RESIDENCIA', max_length=60, blank=True, null=True)
    componente = models.CharField(db_column='COMPONENTE', max_length=60, blank=True, null=True)
    tipo_beca_resumen = models.CharField(db_column='TIPO_BECA_RESUMEN', max_length=60, blank=True, null=True)
    area_ciencia = models.CharField(db_column='AREA_CIENCIA', max_length=60, blank=True, null=True)
    subarea_ciencia = models.CharField(db_column='SUBAREA_CIENCIA', max_length=60, blank=True, null=True)
    sector_prio_conacyt = models.CharField(db_column='SECTOR_PRIO_CONACYT', max_length=60, blank=True, null=True)
    nombre_programa_estudio = models.CharField(db_column='NOMBRE_PROGRAMA_ESTUDIO', max_length=200, blank=True, null=True)
    universidad = models.CharField(db_column='UNIVERSIDAD', max_length=60, blank=True, null=True)
    pais_destino = models.CharField(db_column='PAIS_DESTINO', max_length=60, blank=True, null=True)
    ciudad_destino = models.CharField(db_column='CIUDAD_DESTINO', max_length=60, blank=True, null=True)
    cvpy = models.CharField(db_column='CVPY', max_length=225, blank=True, null=True)

    class Meta:
        managed = False  # ⚠️ No queremos que Django modifique la tabla
        db_table = 'BECAL_IMPORTADO'

