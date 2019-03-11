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


class phone(models.Model):
    '''手机表'''
    phone_name = models.CharField(max_length=128)
    cpu = models.EmailField(unique=False)
    c_time = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.name
 
    class Meta:
        ordering = ['c_time']
        verbose_name = '手机'
        verbose_name_plural = '手机们'