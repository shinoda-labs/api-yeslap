from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'email',
            'password',
            'date_birth',
            'updated_at',
            'created_at'
        )
