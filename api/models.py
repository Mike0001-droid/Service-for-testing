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
    name = models.CharField(
        'Название категории',
        max_length=255
    )
    def __str__(self):
        return f"{self.id}) {self.name}"
    class Meta:
        verbose_name_plural = 'Категории'

class Test (models.Model):
    name = models.CharField(
        'Название теста',
        max_length=255
    )
    description_1 = models.TextField(
        'Описание до'
    )
    description_2 = models.TextField(
        'Описание после'
    )
    comment = models.TextField(
        'Комментарий для преподавателя'
    )
    time_for_solution = models.BooleanField(
        'Записывать время прохождения?'
    )
    necessary_time = models.IntegerField(
        'Необходимое для решения время'
    )
    mix_question = models.BooleanField(
        'Перемешивать вопросы?'
    )
    status = models.CharField(
        'Статус теста',
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"

    class Meta:
        verbose_name_plural = 'Тесты'


class Subtest (models.Model):
    name = models.CharField(
        'Название субтеста',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования субтеста'
    )
    description_1 = models.TextField(
        'Описание до'
    )
    description_2 = models.TextField(
        'Описание после'
    )
    comment = models.TextField(
        'Комментарий для преподавателя'
    )
    time_for_solution = models.BooleanField(
        'Записывать время прохождения?'
    )
    necessary_time = models.IntegerField(
        'Необходимое для решения время'
    )
    mix_question = models.BooleanField(
        'Перемешивать вопросы?'
    )
    status = models.CharField(
        'Статус субтеста',
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='subtests',
        verbose_name='Тест'
    )

    def __str__(self):
        return f" {self.name} "
    
    class Meta:
        verbose_name_plural = 'Субтесты'


class Question (models.Model):
    name = models.CharField(
        'Название вопроса',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования вопроса'
    )
    type_question = models.CharField(
        'Тип вопроса',
        max_length=19, 
        choices=TYPE_CHOICES, 
        default='Единственный выбор'
    )
    obligatory = models.BooleanField(
        'Обязательный ?'
    )
    mix_question = models.BooleanField(
        'Перемешивать вопросы?'
    )
    status = models.CharField(
        'Статус вопроса',
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    subtest = models.ForeignKey(
        Subtest,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Субтест'
    )

    def __str__(self):
        return f" {self.name} "
    
    class Meta:
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    name = models.CharField(
        'Название', max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования ответа'
    )
    right = models.BooleanField(
        'Ответ верный?'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Scale(models.Model):
    name = models.CharField(
        'Название', max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования шкалы'
    )
    score = models.IntegerField(
        'Количество баллов'
    )
    status = models.CharField(
        'Статус шкалы',
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    answer = models.ManyToManyField(
        Answer, verbose_name='Ответ',
        related_name='scale_answer', 
        through='AnswerScale'
    )
    
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Шкала'
        verbose_name_plural = 'Шкалы'

class AnswerScale(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer} : {self.scale}, Кол-во баллов - {self.scale.score}'

    class Meta:
        unique_together = ('answer', 'scale')


class Interpretation (models.Model):
    name = models.CharField(
        'Название интерпретации',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования интерпретации'
    )
    text = models.TextField(
        'Текст'
    )
    start_score = models.IntegerField(
        'Количество баллов от'
    )
    finish_score = models.IntegerField(
        'Количество баллов до')
    status = models.CharField(
        'Статус интерпретации', 
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    scale = models.ForeignKey(
        Scale, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"

    class Meta:
        verbose_name_plural = 'Интерпретации'

class Attemption (models.Model):
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
    """ date = models.DateTimeField(
        'Дата и время прохождения',
        auto_now=True
    )
    time_spent = models.IntegerField(
        'Затраченное время'
    ) """
