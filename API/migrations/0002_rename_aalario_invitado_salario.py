# Generated by Django 4.0.3 on 2022-06-27 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitado',
            old_name='Aalario',
            new_name='Salario',
        ),
    ]