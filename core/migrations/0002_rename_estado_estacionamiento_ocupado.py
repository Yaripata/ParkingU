# Generated by Django 4.2.11 on 2024-06-25 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacionamiento',
            old_name='estado',
            new_name='ocupado',
        ),
    ]
