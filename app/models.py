from django.db import models
from django.utils import timezone 
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class Item(models.Model):
    title = models.CharField(
        "タイトル",
        max_length = 50,
        blank = False,
        null = False,
    )
    content = models.TextField(
        "内容",
        blank = False,
        null = False
    )
    image = models.ImageField(
        "画像",
        blank = False,
        null = False,
    )
    #score = models.PositiveIntegerField("満足度",validators = [MaxValueValidator(100)],blank = False,null = False,)
    
    time = models.DateField(
        "日付"
    )
    user = models.CharField(
        "ユーザー名",
        max_length = 155,
        blank = False,
        null = False,
    )

    def __str__(self):
        return self.title