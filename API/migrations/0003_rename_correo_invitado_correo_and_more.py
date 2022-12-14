# Generated by Django 4.0.3 on 2022-06-30 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_rename_aalario_invitado_salario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitado',
            old_name='Correo',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='invitado',
            old_name='Edad',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='invitado',
            old_name='Genero',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='invitado',
            old_name='Mac',
            new_name='mac',
        ),
        migrations.RenameField(
            model_name='invitado',
            old_name='Salario',
            new_name='salario',
        ),
        migrations.AlterUniqueTogether(
            name='invitado',
            unique_together={('correo', 'mac')},
        ),
    ]
