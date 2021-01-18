from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('detail/<pk>/', views.api_user_detail, name='detail'),
    path('update/<pk>', views.api_user_update, name='update'),
    path('delete/<pk>', views.api_user_delete, name='delete'),
    path('create/', views.api_user_create, name='create'),
]
