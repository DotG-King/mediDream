from django.db import models
from django.contrib.auth.models import User
from accounts.models import MEMBERS
from django.utils import timezone

# Create your models here.

class pillInfo(models.Model):
    pill_name=models.CharField(max_length=50)                               # 이름
    pill_effect=models.TextField(max_length=1000)                           # 효과
    pill_ingredient=models.TextField(max_length=5000, null=True)            # 성분
    pill_usage=models.TextField(max_length=5000)                            # 용법
    medication_information=models.TextField(max_length=5000, null=True)     # 복약정보
    pill_caution=models.TextField(max_length=50000)                         # 주의사항
    pill_color=models.CharField(max_length=50)                              # 색깔
    pill_shape=models.CharField(max_length=50)                              # 모양
    pill_engrave=models.CharField(max_length=50)                            # 각인
    pill_picture=models.URLField(null=True, blank=True)                     # 약학정보원에서 제공하는 알약 사진
    box_picture=models.URLField(null=True, blank=True)                      # 약학정보원에서 제공하는 상자 사진

class search(models.Model):
    mediDream_id=models.ForeignKey(User,on_delete=models.PROTECT,null=True)  # 유저 아이디
    pill=models.ForeignKey(pillInfo,on_delete=models.PROTECT,null=True)         # 약
    date=models.DateTimeField(default=timezone.now)                             # 시간, default 설정
    img= models.ImageField(null=True, blank=True, upload_to='')