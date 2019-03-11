
# Create your models here.

from django.db import models
 
 
class User(models.Model):
    '''用户表'''
 
    gender = (
        ('male','男'),
        ('female','女'),
    )
 
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=False)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'



class Phone(models.Model):
    '''手机表'''
    _id = models.AutoField(primary_key=True,)

    device_name = models.CharField(max_length=128)
    pinpai = models.CharField(max_length=128)
    ram = models.CharField(max_length=128)
    cpu = models.CharField(max_length=128)
    system_version = models.CharField(max_length=128)
    holder_people  = models.CharField(max_length=128)
 
    def __str__(self):
        return self.device_name
 
    class Meta:
        ordering = ['-pinpai']   #加负号表示倒序
        verbose_name = '手机'
        verbose_name_plural = '手机'