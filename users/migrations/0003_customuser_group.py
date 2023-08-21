# Generated by Django 4.2.3 on 2023-08-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.CharField(choices=[('Студент', 'Студент'), ('Преподаватель', 'Преподаватель')], default='Студент', max_length=13, verbose_name='Группа'),
        ),
    ]
