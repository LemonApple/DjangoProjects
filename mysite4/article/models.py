from django.db import models

# Create your models here.
from login.models import Users


class Types(models.Model):
    title = models.CharField(max_length=50)

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="暂无内容！")
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)