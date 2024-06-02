from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view())
]