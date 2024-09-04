from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    date = serializers.CharField()
    avgtemp_c = serializers.FloatField()
    condition_text = serializers.CharField()
    avghumidity = serializers.IntegerField()
    condition_icon = serializers.CharField()