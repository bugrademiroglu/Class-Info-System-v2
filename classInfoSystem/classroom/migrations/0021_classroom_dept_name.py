# Generated by Django 3.0.6 on 2020-05-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0006_auto_20200419_2156'),
        ('classroom', '0020_auto_20200519_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='dept_name',
            field=models.ManyToManyField(to='department.Department', verbose_name='lecture name'),
        ),
    ]
