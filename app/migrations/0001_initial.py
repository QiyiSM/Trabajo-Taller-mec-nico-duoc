# Generated by Django 4.2.2 on 2023-06-27 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('rut', models.CharField(max_length=12)),
                ('correo', models.EmailField(max_length=254)),
                ('imagen', models.ImageField(null=True, upload_to='trabajadores')),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='trabajosproducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='productos')),
                ('nom_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.trabajadores')),
                ('trabajos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.trabajos')),
            ],
        ),
    ]
