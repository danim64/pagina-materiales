# Generated by Django 4.2.3 on 2023-08-02 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'grupos',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=40, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=40, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('vendedor', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name_plural': 'proveedores',
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=150, unique=True)),
                ('precio', models.IntegerField()),
                ('fecha_precio', models.DateTimeField(auto_now=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.grupo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.marca')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.proveedor')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.unidad')),
            ],
            options={
                'verbose_name_plural': 'materiales',
            },
        ),
    ]
