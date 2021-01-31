"""viewのページ
テンプレートをビューで指定する
django.shortcuts MVCの複数のレベルを「橋渡し」するためのヘルパ関数やクラスを定義

ボードを追加



汎用クラスビュー:役割
TemplateView:単純にテンプレートを表示するビュー
ListView:モデルのデータを一覧表示するビュー
DetailView:モデルのデータを個別に詳細表示するビュー
CreateView:モデルにデータを追加するビュー
UpdateView:モデルのデータを更新するビュー
DeleteView:モデルのデータを削除するビュー

"""

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from django.urls import reverse_lazy

from .forms import UserForm, ListForm, CardForm, CardCreateFromHomeForm, BoradForm
from .mixins import OnlyYouMixin
from .models import List, Card, Board


# render(request, template_name, context)はテンプレートに値（変数）を埋め込んだ結果をHttpResponseに変換する関数

def index(request):
    return render(request, "kanban/index.html")



class HomeView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/home.html"


def signup(request):
    # POSTの場合（リクエストが送られた場合）
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # バリデーションを行う
        if form.is_valid():
            # データベースに登録する
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        # フォームクラスをインスタンス化
        form = UserCreationForm()
        context = {
            "form": form
        }
    # context に辞書として定義し render() に渡す
    return render(request, 'kanban/signup.html', context)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "kanban/users/detail.html"


class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('kanban:users_detail', pk=self.kwargs['pk'])


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:lists_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""リストのクラス"""
class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/lists/list.html"


"""リスト詳細クラス"""
class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "kanban/lists/detail.html"


"""リスト編集クラス"""
class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "kanban/lists/update.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:home")


"""リスト削除クラス"""
class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "kanban/lists/delete.html"
    form_class = ListForm
    success_url = reverse_lazy("kanban:home")


"""カード作成クラス"""
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "kanban/cards/list.html"


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "kanban/cards/detail.html"


"""カード編集クラス"""
class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "kanban/cards/update.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")


"""カード削除クラス"""
class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "kanban/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy("kanban:home")


class CardCreateFromHomeView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardCreateFromHomeForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        return super().form_valid(form)


"""ボード作成クラス"""
class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    template_name = "kanban/boards/create.html"
    form_class = BoradForm
    success_url = reverse_lazy("kanban:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

