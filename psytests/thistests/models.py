from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название теста')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class Results(models.Model):
    test_name = models.ForeignKey(Name, on_delete=models.CASCADE, verbose_name='Тест')
    min_score = models.IntegerField(verbose_name='Нижняя граница по баллам')
    max_score = models.IntegerField(verbose_name='Верхняя граница по баллам')
    result = models.CharField(max_length=2000, verbose_name='Вердикт')

    def __str__(self):
        return '{name} ({min}-{max})'.format(name=self.test_name, min=self.min_score, max=self.max_score)

    class Meta:
        verbose_name = 'Результат по тесту'
        verbose_name_plural = 'Результаты по тесту'

class Game(models.Model):
    player_name = models.CharField(max_length=200, verbose_name='ФИО человека')
    test_name = models.ForeignKey(Name, on_delete=models.CASCADE, verbose_name='Тест')
    total_score = models.IntegerField(verbose_name='Сумма баллов')
    result = models.CharField(max_length=2000, verbose_name='Вердикт', default='')

    def __str__(self):
        return '{name} - {test}'.format(name=self.player_name, test=self.test_name)

    class Meta:
        verbose_name = 'Тестирование'
        verbose_name_plural = 'Тестирования'

class Ask(models.Model):
    test_name = models.ForeignKey(Name, on_delete=models.CASCADE, verbose_name='Тест')
    text = models.CharField(max_length=1000, verbose_name='Текст вопроса')

    def __str__(self):
        return '{name}? - {test}'.format(name=self.text, test=self.test_name)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    ask_name = models.ForeignKey(Ask, on_delete=models.CASCADE, verbose_name='Текст вопроса')
    text = models.CharField(max_length=500, verbose_name='Текст ответа')
    score = models.IntegerField(verbose_name='Баллы за ответ')

    def __str__(self):
        return '{name} - {score} ({ask})'.format(name=self.text, score=self.score, ask=self.ask_name)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
