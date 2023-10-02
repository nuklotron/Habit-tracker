from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from habits.models import Habit
from habits.validators import HabitTimeForCompleteValidator, habit_fields_validator
from user.models import User


class HabitListSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Habit
        fields = '__all__'


class HabitSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    validators = [HabitTimeForCompleteValidator(field='time_for_complete'), habit_fields_validator]

    class Meta:
        model = Habit
        fields = '__all__'
