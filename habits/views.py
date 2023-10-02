from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitListSerializer, HabitSerializer
from user.permissions import IsSuper, IsOwner, IsModerator


class HabitCreateAPIView(CreateAPIView):
    """
    CreateAPIView for Habit model.
    Having permissions - IsAuthenticated.
    After create Habit, 'user' field would be filled automatically.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.user = self.request.user
        new_obj.save()


class HabitListAPIView(ListAPIView):
    """
    ListAPIView for Habit model.
    Having permissions - IsAuthenticated.
    If not superuser/moderator showing owner`s object`s
    """
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        super_user = self.request.user.is_superuser
        moderator = self.request.user.groups.filter(name='moderator').exists()
        users_habits = Habit.objects.filter(user=self.request.user)

        if super_user or moderator:
            return self.queryset
        else:
            return users_habits


class HabitPublicListAPIView(ListAPIView):
    """
    ListAPIView for Habit model.
    Having permissions - IsAuthenticated.
    If not superuser/moderator showing public's object`s
    """
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        super_user = self.request.user.is_superuser
        moderator = self.request.user.groups.filter(name='moderator').exists()
        public_habits = Habit.objects.filter(is_public=True)

        if super_user or moderator:
            return self.queryset
        else:
            return public_habits


class HabitDetailAPIView(RetrieveAPIView):
    """
    RetrieveAPIView for Habit model.
    Having permissions - IsAuthenticated, IsOwner or IsSuper.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsSuper]


class HabitUpdateAPIView(UpdateAPIView):
    """
    UpdateAPIView for Habit model.
    Having permissions - IsAuthenticated, IsOwner or IsSuper.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsSuper]


class HabitDeleteAPIView(DestroyAPIView):
    """
    DestroyAPIView for Habit model.
    Having permissions - IsAuthenticated, IsOwner or IsSuper or IsModerator.
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsSuper | IsModerator]
