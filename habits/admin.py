from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'is_pleasant', 'is_public',)
    list_filter = ('user', 'is_pleasant', 'is_public',)
    search_fields = ('user', 'is_pleasant', 'is_public',)

