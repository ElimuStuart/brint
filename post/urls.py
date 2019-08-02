from django.urls import path
from .views import (
    PostList,
    PostCreate,
    PostDetail,
    PostUpdate,
    PostDelete
)

app_name = "post"

urlpatterns = [
    path('posts/', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', PostCreate.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
]
