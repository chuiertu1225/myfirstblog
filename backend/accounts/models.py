from django.db import models
from tool.models import BaseModel
# Create your models here.
class User(BaseModel):

    username = models.CharField('用户名',max_length=100,unique=True)
    password = models.CharField('密码',max_length=128)
    email = models.EmailField('邮箱',blank=True)
    is_super = models.BooleanField('管理员',default=False)
    is_active = models.BooleanField('是否启用',default=True)
    source = models.CharField('创建来源',max_length=100,blank=True)
    age = models.IntegerField('年龄',default=18,blank=True)
    def __str__(self):
        return self.username
    class Meta:
        ordering = ['-created_time']
        verbose_name = '用户'
        verbose_name_plural = verbose_name
