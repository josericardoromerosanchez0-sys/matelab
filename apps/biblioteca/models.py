from django.db import models
from django.contrib.auth import get_user_model
from ..authentication.models import Usuarios

class Biblioteca(models.Model):
    TIPO_CHOICES = [
        ('Practica', 'Practica'),
        ('Juego', 'Juego'),
        ('Contenido', 'Contenido'),
    ]
    
    biblioteca_id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=255, db_column='Titulo')
    descripcion = models.TextField('Descripción', db_column='Descripcion')
    solucion = models.TextField('Solución', db_column='Solucion')
    tipo = models.CharField('Tipo', max_length=50, choices=TIPO_CHOICES, db_column='tipo')
    activo = models.BooleanField('Activo', default=True, db_column='activo')
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='usuario_id')

    class Meta:
        db_table = 'Biblioteca'   
        managed = False  
        verbose_name = 'Contenido de Biblioteca'
        verbose_name_plural = 'Contenidos de Biblioteca' 

    def __str__(self):
        return self.Titulo


class Biblioteca_Usuario(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='usuario_id', primary_key=True)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, db_column='biblioteca_id')
    estado = models.BooleanField('Estado', default=True, db_column='estado')
   
    class Meta:
        db_table = 'Biblioteca_Usuario'   
        managed = False  
        verbose_name = 'Estado de Biblioteca'
        verbose_name_plural = 'Estados de Biblioteca' 
        unique_together = (('usuario', 'biblioteca'),)

    def __str__(self):
        return self.Estado

class Biblioteca_Contenido(models.Model):
    biblioteca_contenido_id = models.AutoField(primary_key=True)
    biblioteca = models.OneToOneField(
        Biblioteca,
        on_delete=models.CASCADE,
        related_name='detalle_contenido'
    )
    teoria = models.TextField('Teoria', db_column='teoria')
    pasos_trucos = models.TextField('Pasos y Trucos', db_column='pasos_trucos')
    ejemplo = models.TextField('Ejemplo', db_column='ejemplo')
    tipo = models.TextField('Tipo', db_column='tipo')
    class Meta:
        db_table = 'Biblioteca_Contenido'   
        managed = False  
        verbose_name = 'Contenido de Biblioteca'
        verbose_name_plural = 'Contenidos de Biblioteca' 
 
    def __str__(self):
        return self.Teoria