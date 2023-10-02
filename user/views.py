from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.models import User
from user.permissions import IsSuper, IsOwner
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for User model (CRUD).

    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    default_permission = [AllowAny]
    permissions = {
        "create": [AllowAny],
        "update": [IsOwner],
        "partial_update": [IsOwner],
        "destroy": [IsSuper],
        "retrieve": [IsAuthenticated],
        "list": [AllowAny],
    }

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.default_permission)
        return super().get_permissions()

    def perform_create(self, serializer):
        new_obj = serializer.save()
        new_obj.set_password(new_obj.password)
        new_obj.save()
