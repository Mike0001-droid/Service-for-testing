from django.db import models
from users.models import MyUser
from django.db.models import F

STATUS_CHOICES = (
    ('черновик', 'черновик'),
    ('опубликовано', 'опубликовано'),
)

TYPE_CHOICES = (
    ('Единственный выбор', 'Единственный выбор'),
    ('Множественный выбор', 'Множественный выбор'),
)


class Category (models.Model):
    name = models.CharField('Название категории', max_length=255)
    queue = models.IntegerField('Порядок')
    status = models.CharField(
        'Статус категории', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    test = models.ManyToManyField(
        'Test', verbose_name='Тест', related_name='category_test', through='CategoryTest')

    def __str__(self):
        return f"{self.id}) {self.name}"

    class Meta:
        verbose_name_plural = '[1] Категории'


class Author (models.Model):
    name = models.CharField('Имя автора', null=True,
                            blank=True, max_length=100)
    last_name = models.CharField(
        'Фамилия автора', null=True, blank=True, max_length=100)
    test = models.ManyToManyField(
        'Test', verbose_name='Тест', related_name='author_test', through='AuthorTest')

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name_plural = '[11] Авторы'


class Topic (models.Model):
    name = models.CharField('Название темы', null=True,
                            blank=True, max_length=255)
    description = models.CharField(
        'Описание темы', null=True, blank=True, max_length=255)
    test = models.ManyToManyField(
        'Test', verbose_name='Тест', related_name='topic_test', through='TopicTest')

    def __str__(self):
        return f"{self.pk}-{self.description}"

    class Meta:
        verbose_name_plural = '[12] Темы'


class Test (models.Model):
    name = models.CharField('Название теста', max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author', verbose_name='Автор', blank=True, null=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name='topic', verbose_name='Тема', blank=True, null=True
    )
    queue = models.IntegerField('Порядок')
    sdescription = models.TextField('Описание до', null=True, blank=True)
    fdescription = models.TextField('Описание после', null=True, blank=True)
    comment = models.TextField(
        'Комментарий для преподавателя', null=True, blank=True)
    time_for_solution = models.BooleanField('Записывать время прохождения?')
    necessary_time = models.IntegerField('Необходимое для решения время')
    mix_question = models.BooleanField('Перемешивать вопросы?')
    subtest = models.ManyToManyField(
        'SubTest', verbose_name='СубТест', related_name='test_subtest', through='TestSubtest')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    status = models.CharField('Статус теста', max_length=12,
                              choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name_plural = '[2] Тесты'
        ordering = ['id']


class Subtest (models.Model):
    name = models.CharField('Название субтеста', max_length=255)
    queue = models.IntegerField('Порядок')
    description = models.TextField('Описание до', null=True, blank=True)
    fdescription = models.TextField('Описание после', null=True, blank=True)
    comment = models.TextField(
        'Комментарий для преподавателя', null=True, blank=True)
    time_for_solution = models.BooleanField('Записывать время прохождения?')
    necessary_time = models.IntegerField('Необходимое для решения время')
    mix_question = models.BooleanField('Перемешивать вопросы?')
    status = models.CharField(
        'Статус субтеста', choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1], max_length=12)
    question = models.ManyToManyField(
        'Question', verbose_name='Вопрос', related_name='subtest_question', through='SubtestQuestion')
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='test', verbose_name='Тест')

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name_plural = '[3] Субтесты'


class Question (models.Model):
    name = models.CharField('Название вопроса', max_length=255)
    queue = models.IntegerField('Порядок')
    question_img = models.ImageField(
        null=True, blank=True, verbose_name='Картинка', upload_to="images/")
    type_question = models.BooleanField(
        'Тип вопроса (Ед.выб/Мн.выб : 1/0)', default=True)
    obligatory = models.BooleanField('Обязательный ?')
    answer = models.ManyToManyField(
        'Answer', verbose_name='Ответы вопроса', blank=True, related_name='answer')
    status = models.CharField(
        'Статус вопроса', choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1], max_length=12)
    subtest = models.ForeignKey(
        Subtest, on_delete=models.CASCADE, related_name='questions', verbose_name='Субтест')

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name_plural = '[4] Вопросы'


class Answer(models.Model):
    name = models.CharField('Название', max_length=255)
    queue = models.IntegerField('Порядок')
    answer_img = models.ImageField(
        null=True, blank=True, upload_to="images/", verbose_name='Картинка')
    status = models.CharField(
        'Статус вопроса', choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1], max_length=12)
    question = models.ManyToManyField(
        Question,
        verbose_name='Вопрос',
        related_name='scale_answer',
        through='QuestionAnswer'
    )

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = '[5] Ответы'
        ordering = ['id']


class Scale(models.Model):
    name = models.CharField('Название', max_length=255)
    queue = models.IntegerField('Порядок')
    status = models.CharField(
        'Статус шкалы', choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1], max_length=12)
    answer = models.ManyToManyField(
        Answer, verbose_name='Ответ', related_name='scale_answer', through='AnswerScale')

    def __str__(self):
        return f"{self.pk}-{self.name}"

    class Meta:
        verbose_name = 'Шкала'
        verbose_name_plural = '[6] Шкалы'


class Score(models.Model):
    score = models.IntegerField('Количество баллов')
    answer = models.ManyToManyField(
        Answer, verbose_name='Баллы', related_name='score_answer', through='AnswerScale')

    def __str__(self):
        return f'{self.score}'

    class Meta:
        verbose_name = 'Балл'
        verbose_name_plural = '[7] Баллы'


class Interpretation (models.Model):
    name = models.CharField('Название интерпретации', max_length=255)
    queue = models.IntegerField('Порядок')
    text = models.TextField('Текст')
    start_score = models.IntegerField('Количество баллов от')
    finish_score = models.IntegerField('Количество баллов до')
    status = models.CharField('Статус интерпретации', choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[1][1], max_length=12)
    scale = models.ForeignKey(
        Scale, on_delete=models.CASCADE, related_name='scales', verbose_name='Шкала')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = '[8] Интерпретации'


class Attemption (models.Model):
    created = models.DateTimeField('Создано', auto_now_add=True)
    user = models.ForeignKey(MyUser, verbose_name='Пользователь',
                             on_delete=models.CASCADE, blank=True, null=True)
    test = models.ForeignKey(Test, verbose_name='Тест',
                             on_delete=models.CASCADE, blank=True)
    answers = models.JSONField(
        'Ответы теста', help_text='JSON формат', null=True, blank=True)

    def formatted_datetime(self):
        return self.created.strftime("%d.%m.%Y")

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name_plural = '[9] Попытки'


class SeoScheme(models.Model):
    key = models.SlugField('Ключ', unique=True)
    name = models.CharField('Описание', max_length=255,
                            help_text='255 символов')
    title = models.CharField(
        max_length=255, help_text='255 символов', null=True, blank=True)
    description = models.CharField(
        max_length=255, help_text='255 символов', null=True, blank=True)
    keywords = models.CharField(
        max_length=255, help_text='255 символов', null=True, blank=True)

    def __str__(self):
        return self.key

    class Meta:
        verbose_name_plural = '[10] Шаблоны для метатегов'


class AnswerScale(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.answer} : {self.scale}, Кол-во баллов - {self.score}'

    class Meta:
        unique_together = ('answer', 'scale', 'score')


class ScaleInterpret(models.Model):
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    interpret = models.ForeignKey(Interpretation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.scale} : {self.interpret}'

    class Meta:
        unique_together = ('scale', 'interpret')


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question} : {self.answer}'

    class Meta:
        unique_together = ('question', 'answer')


class CategoryTest(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} : {self.test}'

    class Meta:
        unique_together = ('category', 'test')


class AuthorTest(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} : {self.test}'

    class Meta:
        unique_together = ('author', 'test')


class TopicTest(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.topic} : {self.test}'

    class Meta:
        unique_together = ('topic', 'test')


class TestSubtest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    subtest = models.ForeignKey(Subtest, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test} : {self.subtest}'

    class Meta:
        unique_together = ('test', 'subtest')


class SubtestQuestion(models.Model):
    subtest = models.ForeignKey(Subtest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subtest} : {self.question}'

    class Meta:
        unique_together = ('subtest', 'question')
