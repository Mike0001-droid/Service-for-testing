# Generated by Django 4.2.7 on 2023-11-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_attemption_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attemption',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.test'),
        ),
    ]
