from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import time

def sesion_path(instance, filename):
    f = time.strftime('/%Y/%m/%d')
    t = time.strftime('/%s') 
    name = instance.name + "_" + filename.replace(" ","_")
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents' + f + t + "_"+ name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    url = models.CharField(max_length=150, verbose_name='Url')
    content = models.TextField(verbose_name='Post')

class Foto(models.Model):
  name = models.CharField(max_length=100, verbose_name='Nombre')
  file = models.FileField(upload_to=sesion_path)
  user = models.ForeignKey(User, related_name="userId")
  created_date = models.DateTimeField(default=timezone.now)