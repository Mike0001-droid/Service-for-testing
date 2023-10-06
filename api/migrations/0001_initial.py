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
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('answer_img', models.ImageField(blank=True, null=True,
                 upload_to='images/', verbose_name='Картинка')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус вопроса')),
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
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255,
                 verbose_name='Название категории')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Опубликовано', max_length=12, verbose_name='Статус категории')),
            ],
            options={
                'verbose_name_plural': '[1] Категории',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255,
                 verbose_name='Название вопроса')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('question_img', models.ImageField(blank=True, null=True,
                 upload_to='images/', verbose_name='Картинка')),
                ('type_question', models.CharField(choices=[('Единственный выбор', 'Единственный выбор'), (
                    'Множественный выбор', 'Множественный выбор')], default='Единственный выбор', max_length=19, verbose_name='Тип вопроса')),
                ('obligatory', models.BooleanField(verbose_name='Обязательный ?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Черновик', max_length=12, verbose_name='Статус вопроса')),
            ],
            options={
                'verbose_name_plural': '[4] Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Черновик', max_length=12, verbose_name='Статус шкалы')),
                ('answer', models.ManyToManyField(related_name='scale_answer',
                 through='api.AnswerScale', to='api.answer', verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Шкала',
                'verbose_name_plural': '[6] Шкалы',
            },
        ),
        migrations.CreateModel(
            name='Subtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255,
                 verbose_name='Название субтеста')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('description_1', models.TextField(
                    blank=True, null=True, verbose_name='Описание до')),
                ('description_2', models.TextField(verbose_name='Описание после')),
                ('comment', models.TextField(
                    verbose_name='Комментарий для преподавателя')),
                ('time_for_solution', models.BooleanField(
                    verbose_name='Записывать время прохождения?')),
                ('necessary_time', models.IntegerField(
                    verbose_name='Необходимое для решения время')),
                ('mix_question', models.BooleanField(
                    verbose_name='Перемешивать вопросы?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Черновик', max_length=12, verbose_name='Статус субтеста')),
            ],
            options={
                'verbose_name_plural': '[3] Субтесты',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    max_length=255, verbose_name='Название теста')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('description_1', models.TextField(verbose_name='Описание до')),
                ('description_2', models.TextField(verbose_name='Описание после')),
                ('comment', models.TextField(blank=True, null=True,
                 verbose_name='Комментарий для преподавателя')),
                ('time_for_solution', models.BooleanField(
                    verbose_name='Записывать время прохождения?')),
                ('necessary_time', models.IntegerField(
                    verbose_name='Необходимое для решения время')),
                ('mix_question', models.BooleanField(
                    verbose_name='Перемешивать вопросы?')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Черновик', max_length=12, verbose_name='Статус теста')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='category', to='api.category', verbose_name='Категория')),
                ('subtest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='subtest', to='api.subtest', verbose_name='Субтест')),
            ],
            options={
                'verbose_name_plural': '[2] Тесты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubtestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('subtest', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.subtest')),
            ],
            options={
                'unique_together': {('subtest', 'question')},
            },
        ),
        migrations.AddField(
            model_name='subtest',
            name='question',
            field=models.ManyToManyField(
                related_name='subtest_question', through='api.SubtestQuestion', to='api.question', verbose_name='Вопрос'),
        ),
        migrations.AddField(
            model_name='subtest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='subtests', to='api.test', verbose_name='Тест'),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(verbose_name='Количество баллов')),
                ('answer', models.ManyToManyField(related_name='score_answer',
                 through='api.AnswerScale', to='api.answer', verbose_name='Баллы')),
            ],
            options={
                'verbose_name': 'Балл',
                'verbose_name_plural': '[7] Баллы',
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.answer')),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
            options={
                'unique_together': {('question', 'answer')},
            },
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(
                related_name='question_answer', through='api.QuestionAnswer', to='api.answer', verbose_name='Ответ'),
        ),
        migrations.AddField(
            model_name='question',
            name='subtest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='questions', to='api.subtest', verbose_name='Субтест'),
        ),
        migrations.CreateModel(
            name='Interpretation',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255,
                 verbose_name='Название интерпретации')),
                ('queue', models.IntegerField(verbose_name='Порядок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('start_score', models.IntegerField(
                    verbose_name='Количество баллов от')),
                ('finish_score', models.IntegerField(
                    verbose_name='Количество баллов до')),
                ('status', models.CharField(choices=[('Черновик', 'Черновик'), (
                    'Опубликовано', 'Опубликовано')], default='Черновик', max_length=12, verbose_name='Статус интерпретации')),
                ('scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='scales', to='api.scale', verbose_name='Шкала')),
            ],
            options={
                'verbose_name_plural': '[8] Интерпретации',
            },
        ),
        migrations.CreateModel(
            name='CategoryTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('test', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
            options={
                'unique_together': {('category', 'test')},
            },
        ),
        migrations.AddField(
            model_name='category',
            name='test',
            field=models.ManyToManyField(
                related_name='category_test', through='api.CategoryTest', to='api.test', verbose_name='Тест'),
        ),
        migrations.AddField(
            model_name='answerscale',
            name='scale',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='api.scale'),
        ),
        migrations.AddField(
            model_name='answerscale',
            name='score',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to='api.score'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='answers', to='api.question', verbose_name='Вопрос'),
        ),
        migrations.CreateModel(
            name='TestSubtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('subtest', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.subtest')),
                ('test', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.test')),
            ],
            options={
                'unique_together': {('test', 'subtest')},
            },
        ),
        migrations.CreateModel(
            name='ScaleInterpret',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('interpret', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.interpretation')),
                ('scale', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='api.scale')),
            ],
            options={
                'unique_together': {('scale', 'interpret')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='answerscale',
            unique_together={('answer', 'scale', 'score')},
        ),
    ]
