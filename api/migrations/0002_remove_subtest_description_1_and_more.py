# Generated by Django 4.2.5 on 2023-10-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtest',
            name='description_1',
        ),
        migrations.RemoveField(
            model_name='subtest',
            name='description_2',
        ),
        migrations.RemoveField(
            model_name='test',
            name='description_1',
        ),
        migrations.RemoveField(
            model_name='test',
            name='description_2',
        ),
        migrations.AddField(
            model_name='subtest',
            name='fdescription',
            field=models.TextField(null=True, verbose_name='Описание после'),
        ),
        migrations.AddField(
            model_name='subtest',
            name='sdescription',
            field=models.TextField(null=True, verbose_name='Описание до'),
        ),
        migrations.AddField(
            model_name='test',
            name='fdescription',
            field=models.TextField(null=True, verbose_name='Описание после'),
        ),
        migrations.AddField(
            model_name='test',
            name='sdescription',
            field=models.TextField(null=True, verbose_name='Описание до'),
        ),
    ]
