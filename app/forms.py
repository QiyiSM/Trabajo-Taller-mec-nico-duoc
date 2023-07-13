from django import forms
from .models import Contacto, Producto , Trabajadores , Trabajos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        

class TrabajadorForm(forms.ModelForm):
    
    class Meta:
        model = Trabajadores
        fields = '__all__'
        
        widgets ={
            "fecha_inicio": forms.SelectDateWidget()
        }
        
class TrabajosForm(forms.ModelForm):
    
    class Meta:
        model = Trabajos 
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", 'password2']
            