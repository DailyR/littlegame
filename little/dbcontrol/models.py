

import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Link(models.Model):
	_id = models.AutoField(primary_key=True,)#unique=True,default=1
	btn_name = models.CharField(max_length=200)
	link_name = models.CharField(max_length=200)
	def __str__(self):
		return self.btn_name

