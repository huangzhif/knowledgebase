from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class knowledges(models.Model):
    title = models.CharField(max_length=500)    #知识点标题
    author = models.ForeignKey(User, related_name='knowledge_post')     #知识点创建人
    body = models.TextField()                       #知识点内容
    created_date = models.DateTimeField(default=timezone.now)   #知识点创建时间

    class Meta:
        ordering = ('-created_date',)    #顺序

    def __str__(self):
        return self.title
