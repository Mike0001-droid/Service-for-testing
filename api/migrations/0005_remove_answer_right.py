# Generated by Django 4.2.3 on 2023-08-31 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_answer_queue_alter_category_queue_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='right',
        ),
    ]
