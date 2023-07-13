from django.contrib import admin
from .models import Producto , Trabajos , Trabajadores , Contacto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = [ "nom_trabajador", "descripcion", "trabajos"]
    list_filter = [ "trabajos" ] 
    list_per_page = 5

class TrabajadoresAdmin(admin.ModelAdmin):
    list_display = [ "nombre", "rut", "correo"]
    list_editable = [ "rut", "correo"]
    search_fields = [ "nombre", "rut", "correo"]
    list_per_page = 5
    
class TrabajosAdmin(admin.ModelAdmin):
    list_display = [ "nombre", "precio" , "tiempo"]
    list_editable = [ "precio" , "tiempo"]
    list_per_page = 5
    
admin.site.register(Producto , ProductoAdmin)
admin.site.register(Trabajos, TrabajosAdmin)
admin.site.register(Trabajadores, TrabajadoresAdmin)
admin.site.register(Contacto)

