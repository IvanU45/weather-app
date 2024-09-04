from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import WeatherSerializer


def get_weather(request):
    if request.method == "POST":
        city = request.POST.get("city")
        api_key = "24a0a74214c14de9808114641240409"
        url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7"
        response = requests.get(url)
        data = response.json()
        return render(request, "weather/weather.html", {"data": data})
    return render(request, "weather/weather.html")

class WeatherAPIView(APIView):
    def get(self, request, city):
        api_key = '24a0a74214c14de9808114641240409'
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            forecast = data.get('forecast', {}).get('forecastday', [])
            serialized_data = [
                {
                    'date': day['date'],
                    'avgtemp_c': day['day']['avgtemp_c'],
                    'condition_text': day['day']['condition']['text'],
                    'avghumidity': day['day']['avghumidity'],
                    'condition_icon': day['day']['condition']['icon']
                }
                for day in forecast
            ]
            serializer = WeatherSerializer(data=serialized_data, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Unable to fetch weather data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
