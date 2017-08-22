from django.contrib.auth.models import User, Group
from facerecognition.models import Post, Foto
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'url')

class FotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foto
        fields = ('name', 'user', 'url', 'created_date','file')