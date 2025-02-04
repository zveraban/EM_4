from rest_framework import serializers
from .models import Dog, Breed

class BreedSerializer(serializers.ModelSerializer):
    dog_count = serializers.IntegerField(read_only=True) 

    class Meta:
        model = Breed
        fields = "__all__"

 
class DogSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source="breed.name", read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    breed_avg_age = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Dog
        fields = "__all__"

 