# Generated by Django 3.0.6 on 2020-05-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0007_auto_20200519_1611'),
        ('classroom', '0018_auto_20200519_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='lecture_date',
            field=models.ManyToManyField(related_name='lecture_start_date', to='lecture.Lecture'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='lecture_date_end',
            field=models.ManyToManyField(related_name='lecture_finish_date', to='lecture.Lecture'),
        ),
    ]
