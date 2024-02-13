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
    description = models.CharField('Описание категории', max_length=255, null=True)
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус',  max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.id}) {self.name}"
    class Meta:
        verbose_name_plural = '[1] Категории'

class Topic (models.Model):
    name = models.CharField('Название темы', null=True, blank=True, max_length=255)
    description = models.CharField('Описание темы', null=True, blank=True, max_length=255)
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус',  max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.pk}-{self.description}"
    class Meta:
        verbose_name_plural = '[2] Темы'

class Test (models.Model):
    name = models.CharField('Название теста', null=True, blank=True, max_length=255)
    author = models.CharField('Автор теста', null=True, blank=True, max_length=100)
    topic = models.ManyToManyField(Topic)
    category = models.ManyToManyField(Category)
    description_1 = models.CharField('Описание до прохождения', null=True, blank=True, max_length=255)
    description_2 = models.CharField('Описание после прохождения', null=True, blank=True, max_length=255)
    comment = models.CharField('Комментарий преподавателя', null=True, blank=True, max_length=255)
    record_time = models.BooleanField('Запись времени прохождения')
    time_for_solution = models.IntegerField('Время для прохождения')
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.pk}) {self.name}"
    class Meta:
        verbose_name_plural = '[3] Тесты'

class Subtest (models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='subtestTest', verbose_name='Тест')
    name = models.CharField('Название субтеста', null=True, blank=True, max_length=255)
    description_1 = models.CharField('Описание до прохождения', null=True, blank=True, max_length=255)
    description_2 = models.CharField('Описание после прохождения', null=True, blank=True, max_length=255)
    comment = models.CharField('Комментарий преподавателя', null=True, blank=True, max_length=255)
    record_time = models.BooleanField('Запись времени прохождения')
    time_for_solution = models.IntegerField('Время для прохождения')
    mix_question = models.BooleanField('Перемешивать вопросы?')
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.pk}) {self.name}"
    class Meta:
        verbose_name_plural = '[4] Субтесты'

class Question (models.Model):
    subtest = models.ForeignKey(Subtest, on_delete=models.CASCADE, related_name='questionSubtest', verbose_name='Субтест')
    name = models.CharField('Название вопроса', max_length=255)
    question_img = models.ImageField(null=True, blank=True, verbose_name='Картинка', upload_to="images/")
    type_question = models.BooleanField('Тип вопроса (Ед.выб/Мн.выб : 1/0)', default=True)
    answer = models.ManyToManyField('PatternAnswer')
    obligatory = models.BooleanField('Обязательный ?')
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.pk}) {self.name}"
    class Meta:
        verbose_name_plural = '[5] Вопросы'

class PatternAnswer (models.Model):
    name = models.CharField('Название', max_length=255)
    answer_img = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name='Картинка')
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f" {self.name} (id = {self.pk})"
    class Meta:
        verbose_name_plural = '[6] Шаблоны ответов'

class Scale (models.Model):
    name = models.CharField('Название', max_length=255)
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    def __str__(self):
        return f"{self.pk}) {self.name}"
    class Meta:
        verbose_name_plural = '[7] Шкала'

class Answer (models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answerTest', verbose_name='Тест')
    patternAnswer = models.ForeignKey(PatternAnswer, on_delete=models.CASCADE, related_name='patternAnswer', verbose_name='Шаблон ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answerQuestion', verbose_name='Вопрос')
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE, related_name='answerScale', verbose_name='Шкала')
    score = models.IntegerField('Количество баллов')
    def __str__(self):
        return f"{self.pk} {self.patternAnswer} ({self.score} бал.)"
    class Meta:
        verbose_name_plural = '[8] Ответы'

class AnswerForQuestion (models.Model):
    user = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)
    answer = models.ForeignKey(Answer, verbose_name='Ответ', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.answer}"
    class Meta:
        verbose_name_plural = '[9] Ответы на вопросы'

class Interpretation (models.Model):
    name = models.CharField('Название', max_length=255, null=True)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE, related_name='interpretationScale', verbose_name='Шкала')
    start_score = models.IntegerField('Кол-во баллов от')
    finish_score = models.IntegerField('Кол-во баллов до')
    description = models.TextField('Текст интерпретации', null=True)
    queue = models.IntegerField('Порядок')
    status = models.CharField('Статус', max_length=12, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][1])
    
    def __str__(self):
        return f"{self.pk}) {self.scale.name}"
    class Meta:
        verbose_name_plural = '[10] Интерпретации'




