# Generated by Django 3.0.6 on 2020-05-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta', '0004_auto_20200523_1729'),
        ('lecture', '0007_auto_20200519_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='ta_name',
            field=models.ManyToManyField(to='ta.TA', verbose_name='Teacher Name'),
        ),
    ]
