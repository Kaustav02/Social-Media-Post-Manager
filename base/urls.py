from django.urls import path
from .views import PostView , PostDetail , CreatePost , UpdatePost , DeltePost , CustomLogin , Register
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('',PostView.as_view(),name='posts'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_details'),
    path('create-post/',CreatePost.as_view(),name='post_create'),
    path('update-post/<int:pk>',UpdatePost.as_view(),name='post_update'),
    path('delete-post/<int:pk>',DeltePost.as_view(),name='post_delete'),
    path('dashboard',views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    
]
