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
    queue = models.IntegerField(
        'Порядок следования Категории'
    )
    status = models.CharField(
        'Статус категории',
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='Черновик'
    )
    test = models.ManyToManyField(
        'Test', 
        verbose_name='Тест',   
        related_name='category_test', 
        through='CategoryTest'
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
    queue = models.IntegerField(
        'Порядок следования теста'
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
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category',
        verbose_name='Категория'
    )
    status = models.CharField(
        'Статус теста',
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='Черновик'
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
        max_length=12,  
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
    answer = models.ManyToManyField(
        'Answer', 
        verbose_name='Ответ',   
        related_name='question_answer', 
        through='QuestionAnswer'
    )
    status = models.CharField(
        'Статус вопроса',
        choices=STATUS_CHOICES,
        max_length=12, 
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
        'Название', 
        max_length=255
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
        'Название', 
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования шкалы'
    )
    status = models.CharField(
        'Статус шкалы',
        choices=STATUS_CHOICES,
        max_length=12,  
        default='Черновик'
    )
    answer = models.ManyToManyField(
        Answer, 
        verbose_name='Ответ',   
        related_name='scale_answer', 
        through='AnswerScale'
    )

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Шкала'
        verbose_name_plural = 'Шкалы'

class Score(models.Model):
    score = models.IntegerField(
        'Количество баллов'
    )
    answer = models.ManyToManyField(
        Answer, 
        verbose_name='Баллы',              
        related_name='score_answer', 
        through='AnswerScale'
    )
    def __str__(self):
        return f'{self.score}'
    class Meta:
        verbose_name = 'Балл'
        verbose_name_plural = 'Баллы'

class AnswerScale(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.answer} : {self.scale}, Кол-во баллов - {self.score}'
    class Meta:
        unique_together = ('answer', 'scale', 'score')

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.question} : {self.answer}'
    class Meta:
        unique_together = ('question','answer')

class CategoryTest(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.category} : {self.test}'
    class Meta:
        unique_together = ('category','test')

class TestSubtest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    subtest = models.ForeignKey(Subtest, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.test} : {self.subtest}'
    class Meta:
        unique_together = ('test','subtest')


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