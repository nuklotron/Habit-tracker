import datetime
import os
import requests
from celery import shared_task
from habits.models import Habit

bot_token = os.getenv('TG_API_KEY')


@shared_task
def send_notifications():
    habits = Habit.objects.filter(user__chat_id__isnull=False)
    time_now = datetime.datetime.now().time()
    t = time_now.strftime("%H:%M:%S")
    for habit in habits:

        print(f'ht - {str(habit.time)}, nt - {str(t)}')
        if str(habit.time) == str(t):

            message = f"I will {habit.action} at {habit.time} in {habit.place}"
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={habit.user.chat_id}" \
                  f"&text={message}"

            response = requests.get(url)

            return response
