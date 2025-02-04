from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели породы (Breed).
    
    Поля:
        dog_count (int, read-only): Количество собак данной породы.
    """
    dog_count = serializers.IntegerField(read_only=True) 

    class Meta:
        model = Breed
        fields = "__all__"

 
class DogSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели собаки (Dog).
    
    Поля:
        breed_name (str, read-only): Название породы собаки.
        same_breed_count (int, read-only): Количество собак той же породы.
        breed_avg_age (float, read-only): Средний возраст собак данной породы.
    """
    breed_name = serializers.CharField(source="breed.name", read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    breed_avg_age = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Dog
        fields = "__all__"

 