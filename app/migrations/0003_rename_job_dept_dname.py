# Generated by Django 4.2.7 on 2023-12-10 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_designation_dept_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dept',
            old_name='job',
            new_name='dname',
        ),
    ]
