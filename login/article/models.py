from django.db import models

# Create your models here.
from loginpage.models import Users


class Types(models.Model):
    title = models.CharField(max_length=50)


class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default="暂无内容")
    type = models.ForeignKey(Types, on_delete=models.CASCADE)  # on_delete=models.CASCADE为实现主外键一致，在Types删除时，文章一并删除
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
