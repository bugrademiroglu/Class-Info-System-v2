# Generated by Django 3.0.6 on 2020-05-19 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0025_auto_20200520_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='department_name',
        ),
    ]
