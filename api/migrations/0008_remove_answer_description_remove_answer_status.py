# Generated by Django 4.2.3 on 2023-08-16 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_answer_status_alter_interpretation_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='status',
        ),
    ]
