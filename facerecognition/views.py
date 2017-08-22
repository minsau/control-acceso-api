from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from facerecognition.serializers import UserSerializer, GroupSerializer, PostSerializer, FotoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from facerecognition.models import Post, Foto
from rest_framework.parsers import MultiPartParser, FormParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
 
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUser,)

class FotosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
      file_obj = request.FILES
      print(file_obj)