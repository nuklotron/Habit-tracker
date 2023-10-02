from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitPublicListAPIView, HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDetailAPIView, HabitDeleteAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('public_list/', HabitPublicListAPIView.as_view(), name='public habits list'),
    path('my_list/', HabitListAPIView.as_view(), name='users habits list'),
    path('create/', HabitCreateAPIView.as_view(), name='create habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update habit'),
    path('view/<int:pk>/', HabitDetailAPIView.as_view(), name='detail habit'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='delete habit'),
]
