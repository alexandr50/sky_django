from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserProfileView, UserRegisterView, generate_password, confirm_code

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/confirm_code/<str:email>/', confirm_code, name='confirm_code'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/generate_password', generate_password, name='generate_password'),

]