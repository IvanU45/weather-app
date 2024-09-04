from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_weather, name='get_weather'),
    path('api/weather/<str:city>/', views.WeatherAPIView.as_view(), name='weather-api')
]