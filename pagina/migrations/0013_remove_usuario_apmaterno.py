# Generated by Django 4.1.2 on 2024-06-30 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0012_rename_appaterno_usuario_apellido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apMaterno',
        ),
    ]