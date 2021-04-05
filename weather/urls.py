from django.urls import path

from .views import IndexView, LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login-override'),
    path('<int:pk>', IndexView.as_view(), name='city_weather'),
    path('', IndexView.as_view(), name='index')
]