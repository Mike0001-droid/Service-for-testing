# Generated by Django 4.2.7 on 2023-11-22 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('answer_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус вопроса')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': '[5] Ответы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AnswerScale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус категории')),
            ],
            options={
                'verbose_name_plural': '[1] Категории',
            },
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название интерпретации')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('start_score', models.IntegerField(verbose_name='Количество баллов от')),
                ('finish_score', models.IntegerField(verbose_name='Количество баллов до')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус интерпретации')),
            ],
            options={
                'verbose_name_plural': '[8] Интерпретации',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название вопроса')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('question_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('type_question', models.BooleanField(default=True, verbose_name='Тип вопроса (Ед.выб/Мн.выб : 1/0)')),
                ('obligatory', models.BooleanField(verbose_name='Обязательный ?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус вопроса')),
            ],
            options={
                'verbose_name_plural': '[4] Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус шкалы')),
                ('balls', models.IntegerField(default=0, verbose_name='Количество набранных баллов')),
                ('answer', models.ManyToManyField(related_name='scale_answer', through='api.AnswerScale', to='api.answer', verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Шкала',
                'verbose_name_plural': '[6] Шкалы',
            },
        ),
        migrations.CreateModel(
            name='Subtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название субтеста')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('sdescription', models.TextField(blank=True, null=True, verbose_name='Описание до')),
                ('fdescription', models.TextField(blank=True, null=True, verbose_name='Описание после')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий для преподавателя')),
                ('time_for_solution', models.BooleanField(verbose_name='Записывать время прохождения?')),
                ('necessary_time', models.IntegerField(verbose_name='Необходимое для решения время')),
                ('mix_question', models.BooleanField(verbose_name='Перемешивать вопросы?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус субтеста')),
            ],
            options={
                'verbose_name_plural': '[3] Субтесты',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название теста')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Автор теста')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('sdescription', models.TextField(blank=True, null=True, verbose_name='Описание до')),
                ('fdescription', models.TextField(blank=True, null=True, verbose_name='Описание после')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий для преподавателя')),
                ('time_for_solution', models.BooleanField(verbose_name='Записывать время прохождения?')),
                ('necessary_time', models.IntegerField(verbose_name='Необходимое для решения время')),
                ('mix_question', models.BooleanField(verbose_name='Перемешивать вопросы?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), ('Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус теста')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': '[2] Тесты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TestSubtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subtest')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='subtest',
            field=models.ManyToManyField(related_name='test_subtest', through='api.TestSubtest', to='api.subtest', verbose_name='СубТест'),
        ),
        migrations.CreateModel(
            name='SubtestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subtest')),
            ],
        ),
        migrations.AddField(
            model_name='subtest',
            name='question',
            field=models.ManyToManyField(related_name='subtest_question', through='api.SubtestQuestion', to='api.question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='subtest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='api.test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Количество баллов')),
                ('answer', models.ManyToManyField(related_name='score_answer', through='api.AnswerScale', to='api.answer', verbose_name='Баллы')),
            ],
            options={
                'verbose_name': 'Балл',
                'verbose_name_plural': '[7] Баллы',
            },
        ),
        migrations.CreateModel(
            name='ScaleInterpret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interpret', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.interpretation')),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.scale')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(related_name='question_answer', through='api.QuestionAnswer', to='api.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='question',
            name='subtest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.subtest', verbose_name='Субтест'),
        ),
        migrations.AddField(
            model_name='interpretation',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scales', to='api.scale', verbose_name='Шкала'),
        ),
        migrations.CreateModel(
            name='CategoryTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='test',
            field=models.ManyToManyField(related_name='category_test', through='api.CategoryTest', to='api.test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='Attemption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.ManyToManyField(blank=True, related_name='answer', to='api.answer', verbose_name='Ответы теста')),
                ('test', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.test', verbose_name='Тест')),
            ],
            options={
                'verbose_name_plural': 'Попытки',
            },
        ),
    ]
