from django.db import models
from django.utils import timezone
from django.urls import reverse


class Story(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    instruction = models.TextField(max_length=400, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('story-detail', kwargs={'pk': self.pk})


class Question(models.Model):
    # ANSWER = 'A'
    # WRONG = 'W'

    # ANSWER_SELECTOR = (
    #     (ANSWER, 'Correct Answer'),
    #     (WRONG, 'Wrong Answer')
    # )

    story_content = models.ForeignKey(Story, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    # options = models.ForeignKey('Option', on_delete=models.CASCADE)
    option_one = models.CharField(max_length=80)
    option_one_is_answer = models.BooleanField('Is Option One The Answer?', default=False)
    option_two = models.CharField(max_length=80)
    option_two_is_answer = models.BooleanField('Is Option Two The Answer?', default=False)
    option_three = models.CharField(max_length=80)
    option_three_is_answer = models.BooleanField('Is Option Three The Answer?', default=False)
    option_four = models.CharField(max_length=80)
    option_four_is_answer = models.BooleanField('Is Option Four The Answer?', default=False)
    point = models.IntegerField(default=0)
    count = models.PositiveIntegerField(default=0)
    max_question = models.PositiveIntegerField(default=10)
    # answer = models.OneToOneField('Option', on_delete=models.CASCADE, related_name='correct_answer')
    date = models.DateTimeField(default=timezone.now)
    duration = models.FloatField(default=30)

    def __str__(self):
        return self.question


class Test(models.Model):
    full_name = models.CharField('Full Name', max_length=100)
    test_questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

