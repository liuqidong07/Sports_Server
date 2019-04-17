from django.db import models

# Create your models here.

class user_information(models.Model):
    id = models.AutoField(primary_key=True)
    openid = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20, null=True)
    gender = models.IntegerField(null=True)
    city = models.CharField(null=True,max_length=20)
    province = models.CharField(null=True,max_length=20)
    country = models.CharField(null=True,max_length=20)
    portrait = models.URLField(null=True)

