from django.urls import path, include
from post.views import PostList, PostCreate, PostDelete, PostDetail, PostUpdate, PostView

from rest_framework import routers

app_name = 'post'

router = routers.DefaultRouter()
router.register('posts', PostView)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/create/', PostCreate.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),
]

api_urlpatterns = [
    path('api/', include(router.urls)),
]

urlpatterns += api_urlpatterns
