from django.db import models
from user.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, verbose_name='creator of habit', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='where habit needs to be complete')
    time = models.TimeField(verbose_name='when the habit needs to be complete')
    action = models.CharField(max_length=150, verbose_name='action that constitutes a habit')
    is_pleasant = models.BooleanField(default=True, verbose_name='is habit is pleasant')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='if habit related with another',
                                      **NULLABLE)
    periodicity = models.SmallIntegerField(default=1, verbose_name='periodicity of habit execution')
    reward = models.CharField(max_length=150, verbose_name='reward for habit complete', **NULLABLE)
    time_for_complete = models.TimeField(verbose_name='time to complete habit')
    is_public = models.BooleanField(default=True, verbose_name='is habit is public')

    def __str__(self):
        return f'Habit of {self.user} need to be complete at {self.place}'

    class Meta:
        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
        ordering = ['pk']
