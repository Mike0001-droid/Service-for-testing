# Generated by Django 4.2.3 on 2023-08-29 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_question_mix_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['id'], 'verbose_name_plural': '2) Тесты'},
        ),
    ]
