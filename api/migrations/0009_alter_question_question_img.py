# Generated by Django 4.2.3 on 2023-08-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_answer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
