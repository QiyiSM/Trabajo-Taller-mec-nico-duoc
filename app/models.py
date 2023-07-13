from django.db import models

# Create your models here.

class Trabajos(models.Model):
    nombre = models.CharField(max_length=50)
    tiempo = models.CharField(max_length=50,  null=True)
    precio = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Trabajadores(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    tra = models.ForeignKey(Trabajos, on_delete=models.PROTECT ,  null=True)
    rut = models.CharField(max_length=12)
    correo = models.EmailField(max_length=254)
    fecha_inicio = models.DateField()
    imagen = models.ImageField(upload_to="trabajadores", null=True)
    
    
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nom_trabajador = models.ForeignKey(Trabajadores, on_delete=models.PROTECT)
    descripcion = models.TextField()
    trabajos = models.ForeignKey(Trabajos, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="productos", null=True)
        
    def __str__(self):
        return self.nom_trabajador.nombre
    
    
opciones_consultas = [
    [0, "consulta"  ],
    [1, "reclamo"  ],  
    [2, "sugerencia"  ],  
    [3, "felicitaciones"  ]      
]    
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    