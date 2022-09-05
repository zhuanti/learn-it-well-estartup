# from django.db import models
#
# # Create your models here.
#
from django.db import models
#
#
# 使用者資訊
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=5)
    live = models.CharField(max_length=100)
    photo = models.TextField(blank=True, null=True)
    borth = models.DateField(blank=True, null=True)
    purview = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'
