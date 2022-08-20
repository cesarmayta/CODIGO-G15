from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Miembro(models.Model):
    miembro_id = models.AutoField(primary_key=True)
    usuario_id = models.OneToOneField(User,to_field='id',on_delete=models.RESTRICT,verbose_name='Usuario')
    miembro_titulo = models.CharField(max_length=200,verbose_name='Titulo')
    miembro_biografia = models.TextField()
    miembro_twitter = models.CharField(max_length=100,verbose_name='Twitter')
    miembro_facebook = models.CharField(max_length=100,verbose_name='Facebook')
    miembro_youtube = models.CharField(max_length=100,verbose_name='Youtube')
    miembro_github = models.CharField(max_length=100,verbose_name='GitHub')
    miembro_sitioweb = models.CharField(max_length=100,verbose_name='Sitio Web')
    miembro_imagen = CloudinaryField('image',default='')

    class Meta:
        db_table = 'tbl_miembro'

    def __str__(self):
        return self.miembro_titulo

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    categoria_nombre = models.CharField(max_length=200,verbose_name='Nombre')

    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.categoria_nombre

class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    curso_titulo = models.CharField(max_length=255,verbose_name='Titulo')
    curso_descripcion = models.TextField()
    curso_resumen = models.TextField()
    curso_precio = models.DecimalField(max_digits=10,decimal_places=2)
    curso_imagen = CloudinaryField('image',default='')
    autor_id = models.ForeignKey(Miembro,to_field='miembro_id',on_delete=models.RESTRICT,verbose_name='Autor')

    class Meta:
        db_table = 'tbl_curso'

    def __str__(self):
        return self.curso_titulo


    
