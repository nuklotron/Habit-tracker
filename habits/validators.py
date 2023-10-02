from datetime import time
from rest_framework.exceptions import ValidationError


class HabitTimeForCompleteValidator:
    """
    Time for complete habit should be less than 2 min
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field):
            if dict(value).get(self.field) > time(00, 2):
                raise ValidationError('Time for complete should be less than 2 min')


def habit_fields_validator(value):
    if value.get('related_habit') and value.get('reward'):
        raise ValidationError('You can`t assign reward for related habit')
    if value.get('related_habit'):
        if not value.get('related_habit').is_pleasant:
            raise ValidationError('Only pleasant habits can be related')
    if value.get('is_pleasant') or 'is_pleasant' not in value:
        if value.get('reward'):
            raise ValidationError('You can`t reward pleasant habit')
        if value.get('related_habit'):
            raise ValidationError('Pleasant habit can`t relate with other habits')
    if value.get('periodicity'):
        if value.get('periodicity') > 7:
            raise ValidationError('You cannot perform the habit less than once every 7 days')
