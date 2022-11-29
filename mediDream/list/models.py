from django.db import models
from django.contrib.auth.models import User
from accounts.models import MEMBERS
from django.utils import timezone

# Create your models here.

class pillInfo(models.Model):
    pill_name=models.CharField(max_length=50)       # 이름
    pill_effect=models.CharField(max_length=250)    # 효과
    pill_usage=models.CharField(max_length=250)     # 용법
    pill_caution=models.CharField(max_length=255)   # 주의사항
    pill_color=models.CharField(max_length=50)      # 색깔
    pill_shape=models.CharField(max_length=50)      # 모양
    pill_engrave=models.CharField(max_length=50)    # 각인        

class search(models.Model):
    mediDream_id=models.ForeignKey(User,on_delete=models.PROTECT,null=True)  # 유저 아이디
    pill=models.ForeignKey(pillInfo,on_delete=models.PROTECT,null=True)         # 약
    date=models.DateTimeField(default=timezone.now)                             # 시간, default 설정
    img= models.ImageField(null=True, blank=True, upload_to='')