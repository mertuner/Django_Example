from django.urls import path
from lvl5app import views

app_name = 'lvl5app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
]
