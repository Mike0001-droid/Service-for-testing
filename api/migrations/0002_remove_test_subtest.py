# Generated by Django 4.2.3 on 2023-10-04 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='subtest',
        ),
    ]