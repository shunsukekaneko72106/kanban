"""
リストモデルを追加
コンフリクトしてたので影響があるかも

"""



from django.contrib.auth.models import User
from django.db import models

"""リストモデル"""
class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title






"""カードクラス"""
class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





