# Generated by Django 5.0 on 2024-02-13 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Описание категории')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': '[1] Категории',
            },
        ),
        migrations.CreateModel(
            name='PatternAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('answer_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': '[6] Шаблоны ответов',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': '[7] Шкала',
            },
        ),
        migrations.CreateModel(
            name='Subtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название субтеста')),
                ('description_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание до прохождения')),
                ('description_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание после прохождения')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий преподавателя')),
                ('record_time', models.BooleanField(verbose_name='Запись времени прохождения')),
                ('time_for_solution', models.IntegerField(verbose_name='Время для прохождения')),
                ('mix_question', models.BooleanField(verbose_name='Перемешивать вопросы?')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': '[4] Субтесты',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название темы')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание темы')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': '[2] Темы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название вопроса')),
                ('question_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('type_question', models.BooleanField(default=True, verbose_name='Тип вопроса (Ед.выб/Мн.выб : 1/0)')),
                ('obligatory', models.BooleanField(verbose_name='Обязательный ?')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
                ('answer', models.ManyToManyField(to='api.patternanswer')),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionSubtest', to='api.subtest', verbose_name='Субтест')),
            ],
            options={
                'verbose_name_plural': '[5] Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название теста')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Автор теста')),
                ('description_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание до прохождения')),
                ('description_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание после прохождения')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий преподавателя')),
                ('record_time', models.BooleanField(verbose_name='Запись времени прохождения')),
                ('time_for_solution', models.IntegerField(verbose_name='Время для прохождения')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('черновик', 'черновик'), ('опубликовано', 'опубликовано')], default='опубликовано', max_length=12, verbose_name='Статус')),
                ('category', models.ManyToManyField(to='api.category')),
                ('topic', models.ManyToManyField(to='api.topic')),
            ],
            options={
                'verbose_name_plural': '[3] Тесты',
            },
        ),
        migrations.AddField(
            model_name='subtest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtestTest', to='api.test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Количество баллов')),
                ('patternAnswer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patternAnswer', to='api.patternanswer', verbose_name='Шаблон ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answerQuestion', to='api.question', verbose_name='Вопрос')),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answerScale', to='api.scale', verbose_name='Шкала')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answerTest', to='api.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name_plural': '[8] Ответы',
            },
        ),
    ]
