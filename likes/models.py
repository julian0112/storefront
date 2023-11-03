from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class LikedItems(models.Model):
    #Generic relationship structure
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    #Generic user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
