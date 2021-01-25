"""viewのページ
テンプレートをビューで指定する
django.shortcuts MVCの複数のレベルを「橋渡し」するためのヘルパ関数やクラスを定義

"""

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import DetailView, UpdateView

from .forms import UserForm

#render(request, template_name, context)はテンプレートに値（変数）を埋め込んだ結果をHttpResponseに変換する関数

def index(request):
    return render(request, "kanban/index.html")

#デコレーターでログインを呼び出し
@login_required
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    #POSTの場合（リクエストが送られた場合）
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #バリデーションを行う
        if form.is_valid():
            #データベースに登録する
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        #フォームクラスをインスタンス化
        form = UserCreationForm()
        context = {
            "form": form
        }
    #context に辞書として定義し render() に渡す
    return render(request, 'kanban/signup.html', context)


class UserDetailView(DetailView):
    model = User
    template_name = "kanban/users/detail.html"


class UserUpdateView(UpdateView):
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])


