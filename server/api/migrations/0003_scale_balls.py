# Generated by Django 4.2.7 on 2023-11-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_answer_attemption_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='scale',
            name='balls',
            field=models.IntegerField(default=0, verbose_name='Количество набранных баллов'),
        ),
    ]
