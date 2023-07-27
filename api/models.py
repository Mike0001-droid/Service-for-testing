from django.db import models


class Category (models.Model):
    name = models.CharField(
        'Название категории',
        max_length=255
    )


class Test (models.Model):
    name = models.CharField(
        'Название теста',
        max_length=255
    )
    description_1 = models.CharField(
        'Описание до',
        max_length=255
    )
    description_2 = models.CharField(
        'Описание после',
        max_length=255
    )
    comment = models.CharField(
        'Комментарий для преподавателя',
        max_length=255
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
        max_length=255
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"


class Subtest (models.Model):
    name = models.CharField(
        'Название субтеста',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования субтеста'
    )
    description_1 = models.CharField(
        'Описание до',
        max_length=255
    )
    description_2 = models.CharField(
        'Описание после',
        max_length=255
    )
    comment = models.CharField(
        'Комментарий для преподавателя',
        max_length=255
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
        max_length=255
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"


class Questions (models.Model):
    name = models.CharField(
        'Название вопроса',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования вопроса'
    )
    type_question = models.CharField(
        'Тип вопроса',
        max_length=255
    )
    obligatory = models.BooleanField(
        'Обязательный ?'
    )
    mix_question = models.BooleanField(
        'Перемешивать вопросы?'
    )
    status = models.CharField(
        'Статус вопроса',
        max_length=255
    )
    subtest = models.ForeignKey(
        Subtest,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"


class Answers (models.Model):
    name = models.CharField(
        'Название ответа',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования ответа'
    )
    description = models.CharField(
        'Описание ответа',
        max_length=255
    )
    score = models.IntegerField(
        'Количество баллов'
    )
    right = models.BooleanField(
        'Ответ верный?'
    )
    status = models.CharField(
        'Статус ответа',
        max_length=255
    )
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"


class Scales (models.Model):
    name = models.CharField(
        'Название шкалы',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования шкалы'
    )
    description = models.CharField(
        'Описание шкалы',
        max_length=255
    )
    status = models.CharField(
        'Статус шкалы',
        max_length=255
    )
    answers = models.ForeignKey(
        Answers,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.id}) {self.name}"


class Interpretations (models.Model):
    name = models.CharField(
        'Название интерпретации',
        max_length=255
    )
    queue = models.IntegerField(
        'Порядок следования интерпретации'
    )
    text = models.CharField(
        'Текст',
        max_length=255
    )
    start_score = models.IntegerField(
        'Количество баллов от'
    )
    finish_score = models.IntegerField(
        'Количество баллов до')
    status = models.CharField('Статус интерпретации', max_length=255)
    scale = models.ForeignKey(Scales, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}) {self.name}"


class Attemption (models.Model):
    number = models.IntegerField(
        'Номер попытки'
    )
    date = models.DateTimeField(
        'Дата и время прохождения',
        auto_now=True
    )
    time_spent = models.IntegerField(
        'Затраченное время'
    )
    """ user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    ) """
    test = models.OneToOneField(
        Test,
        on_delete=models.CASCADE
    )
    question = models.OneToOneField(
        Questions,
        on_delete=models.CASCADE
    )
    answer = models.OneToOneField(
        Answers,
        on_delete=models.CASCADE
    )
    scale = models.OneToOneField(
        Scales,
        on_delete=models.CASCADE
    )
    interpretation = models.OneToOneField(
        Interpretations,
        on_delete=models.CASCADE
    )
