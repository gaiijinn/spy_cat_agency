from rest_framework import serializers
from django.core.cache import cache
from .models import Cat
import requests


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

    def validate_breed(self, value):
        breeds = cache.get('cat_breeds')

        if not breeds:
            response = requests.get('https://api.thecatapi.com/v1/breeds')

            if response.status_code != 200:
                raise serializers.ValidationError("CatsAPI doesn't reply, try again later")

            breeds = response.json()
            cache.set('cat_breeds', breeds, timeout=3600)

        breed_names = [breed['name'].lower() for breed in breeds]
        if value.lower() not in breed_names:
            raise serializers.ValidationError(f"Breed '{value}' doesn't exist")

        return value
