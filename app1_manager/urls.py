from django.urls import path
from .views import simple_page,PostList, PostDetail

urlpatterns = [
    path('simple-page/', simple_page, name='simple_page'),
     path('simple-api/', PostList.as_view(), name='post_list'),
    path('simple-api/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]