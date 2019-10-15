from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.model import Chat


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',)


class ChatListSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = ('room_id',
                  'room_id_id')


class UserListSerializer(ModelSerializer):
    chat_set = ChatListSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'chat_set')

