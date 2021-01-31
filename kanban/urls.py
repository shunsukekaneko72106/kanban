"""
ルーティングの設定

ボードの追加
"""


from django.urls import path

from . import views

app_name = "kanban"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.HomeView.as_view(), name="home"),
    path('signup/', views.signup, name='signup'),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
    path("lists/", views.ListListView.as_view(), name="lists_list"),
    path("lists/create/", views.ListCreateView.as_view(), name="lists_create"),
    path("lists/<int:pk>/", views.ListDetailView.as_view(), name="lists_detail"),
    path("lists/<int:pk>/update/", views.ListUpdateView.as_view(), name="lists_update"),
    path("lists/<int:pk>/delete/", views.ListDeleteView.as_view(), name="lists_delete"),
    path("cards/create/", views.CardCreateView.as_view(), name="cards_create"),
    path("cards/", views.CardListView.as_view(), name="cards_list"),
    path("cards/<int:pk>/", views.CardDetailView.as_view(), name="cards_detail"),
    path("cards/<int:pk>/update/", views.CardUpdateView.as_view(), name="cards_update"),
    path("cards/<int:pk>/delete/", views.CardDeleteView.as_view(), name="cards_delete"),
    path("cards/create/<int:list_pk>", views.CardCreateFromHomeView.as_view(), name="cards_create_from_home"),
    path("boards/create/", views.BoardCreateView.as_view(), name="boards_create"),
    path("boards/", views.BoardListView.as_view(), name="boards_list"),
    path("boards/<int:pk>/", views.BoardDetailView.as_view(), name="boards_detail"),
    path("boards/<int:pk>/update/", views.BoardUpdateView.as_view(), name="boards_update"),
    path("boards/<int:pk>/delete/", views.BoardDeleteView.as_view(), name="boards_delete"),


]


