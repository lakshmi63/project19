# Generated by Django 4.2.7 on 2023-12-10 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dept',
            old_name='designation',
            new_name='job',
        ),
    ]
