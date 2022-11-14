from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .serializers import GroupSerializer, UserXsSerializer

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserXsSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            qs = User.objects.filter(is_removed=False)
        else:
            qs = User.objects.filter(id=self.request.user.id, is_removed=False)
        return qs


class GroupViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
