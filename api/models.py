from django.db import models
from users.models import CustomUser
from django.db.models import F

STATUS_CHOICES = (
    ('Черновик', 'Черновик'),
    ('Опубликовано', 'Опубликовано'),
)

TYPE_CHOICES = (
    ('Единственный выбор', 'Единственный выбор'),
    ('Множественный выбор', 'Множественный выбор'),
)


class Category (models.Model):
    name = models.CharField('Название категории', max_length=255)
    queue = models.IntegerField('Порядок')
    status = models.CharField(
        'Статус категории', max_length=12, choices=STATUS_CHOICES, default='Опубликовано')
    test = models.ManyToManyField(
        'Test', verbose_name='Тест', related_name='category_test', through='CategoryTest')

    def __str__(self):
        return f"{self.id}) {self.name}"

    class Meta:
        verbose_name_plural = '[1] Категории'


class Test (models.Model):
    name = models.CharField('Название теста', max_length=255)
    queue = models.IntegerField('Порядок')
    sdescription = models.TextField('Описание до', null=True)
    fdescription = models.TextField('Описание после', null=True)
    comment = models.TextField(
        'Комментарий для преподавателя', null=True, blank=True)
    time_for_solution = models.BooleanField('Записывать время прохождения?')
    necessary_time = models.IntegerField('Необходимое для решения время')
    mix_question = models.BooleanField('Перемешивать вопросы?')
    subtest = models.ManyToManyField(
        'SubTest', verbose_name='СубТест', related_name='test_subtest', through='TestSubtest')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category', verbose_name='Категория')
    status = models.CharField(
        'Статус теста', max_length=12, choices=STATUS_CHOICES, default='Черновик')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = '[2] Тесты'
        ordering = ['id']


class Subtest (models.Model):
    name = models.CharField('Название субтеста', max_length=255)
    queue = models.IntegerField('Порядок')
    sdescription = models.TextField('Описание до', null=True)
    fdescription = models.TextField('Описание после', null=True)
    comment = models.TextField('Комментарий для преподавателя')
    time_for_solution = models.BooleanField('Записывать время прохождения?')
    necessary_time = models.IntegerField('Необходимое для решения время')
    mix_question = models.BooleanField('Перемешивать вопросы?')
    status = models.CharField(
        'Статус субтеста', choices=STATUS_CHOICES, max_length=12, default='Черновик')
    question = models.ManyToManyField(
        'Question', verbose_name='Вопрос', related_name='subtest_question', through='SubtestQuestion')
    test = models.ForeignKey(
        Test, on_delete=models.CASCADE, related_name='test', verbose_name='Тест')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = '[3] Субтесты'


class Question (models.Model):
    name = models.CharField('Название вопроса', max_length=255)
    queue = models.IntegerField('Порядок')
    question_img = models.ImageField(
        null=True, blank=True, verbose_name='Картинка', upload_to="images/")
    type_question = models.CharField(
        'Тип вопроса', max_length=19, choices=TYPE_CHOICES, default='Единственный выбор')
    obligatory = models.BooleanField('Обязательный ?')
    answer = models.ManyToManyField(
        'Answer', verbose_name='Ответ', related_name='question_answer', through='QuestionAnswer')
    status = models.CharField(
        'Статус вопроса', choices=STATUS_CHOICES, max_length=12, default='Черновик')
    subtest = models.ForeignKey(
        Subtest, on_delete=models.CASCADE, related_name='questions', verbose_name='Субтест')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = '[4] Вопросы'


class Answer(models.Model):
    name = models.CharField('Название', max_length=255)
    queue = models.IntegerField('Порядок')
    answer_img = models.ImageField(
        null=True, blank=True, upload_to="images/", verbose_name='Картинка')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', verbose_name='Вопрос')
    status = models.CharField(
        'Статус вопроса', choices=STATUS_CHOICES, max_length=12, default='Опубликовано')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = '[5] Ответы'
        ordering = ['id']


class Scale(models.Model):
    name = models.CharField('Название', max_length=255)
    queue = models.IntegerField('Порядок')
    status = models.CharField(
        'Статус шкалы', choices=STATUS_CHOICES, max_length=12, default='Черновик')
    answer = models.ManyToManyField(
        Answer, verbose_name='Ответ', related_name='scale_answer', through='AnswerScale')

    def __str__(self):
        return f'{self.name}'

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
    status = models.CharField(
        'Статус интерпретации', choices=STATUS_CHOICES, default='Черновик', max_length=12)
    scale = models.ForeignKey(
        Scale, on_delete=models.CASCADE, related_name='scales', verbose_name='Шкала')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = '[8] Интерпретации'


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


""" class Attemption (models.Model):
    number = models.IntegerField(
        'Номер попытки',
        default=0
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    test = models.OneToOneField(
        Test,
        unique=False,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name_plural = 'Попытки'

    date = models.DateTimeField(
        'Дата и время прохождения',
        auto_now=True
    )
    time_spent = models.IntegerField(
        'Затраченное время'
    ) 
 """
