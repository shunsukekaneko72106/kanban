"""
リストモデル（デフォルト）
カードモデル（デフォルト）

ボードモデル追加

"""



from django.contrib.auth.models import User
from django.db import models


"""ボードモデル"""
class Board(models.Model):
    #タイトルをCharFieldは文字列型でmax_length（最大文字数）を表す
    title = models.CharField(max_length=50)
    #ユーザーForeignKeyは一対多を表現するリレーションシップ型、第一引数にリレーション先のモデル、on_delete引数でデータ削除時の挙動を指定
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #クリエイトされた日時
    created = models.DateField(auto_now_add=True)
    #更新された日時
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


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





