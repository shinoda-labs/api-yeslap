from rest_framework.viewsets import ModelViewSet

from user.api.serializers import UserSerializer
from user.models import User


class UserViewset(ModelViewSet):
    queryset = User.objects.all().order_by('created_at')
    serializer_class = UserSerializer
