from django.db import models
from django.contrib.auth import get_user_model
from ..authentication.models import Usuarios

class Biblioteca(models.Model):
    TIPO_CHOICES = [
        ('Practica', 'Practica'),
        ('Juego', 'Juego'), 
    ]
    
    # Asegúrate de que los nombres de los campos coincidan exactamente con tu base de datos
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=255, db_column='Titulo')
    descripcion = models.TextField('Descripción', db_column='Descripcion')
    solucion = models.TextField('Solución', db_column='Solucion')
    tipo = models.CharField('Tipo', max_length=50, choices=TIPO_CHOICES, db_column='tipo')
    activo = models.BooleanField('Activo', default=True, db_column='activo')
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='usuario_id')
   
    class Meta:
        db_table = 'Biblioteca'  # Nombre exacto de la tabla en SQL Server
        managed = False  # Le dice a Django que no maneje la creación/eliminación de la tabla
        verbose_name = 'Contenido de Biblioteca'
        verbose_name_plural = 'Contenidos de Biblioteca' 

    def __str__(self):
        return self.Titulo