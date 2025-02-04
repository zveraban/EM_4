from rest_framework import viewsets
from django.db.models import Avg, Count, Subquery, OuterRef
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.annotate(dog_count=Count("dogs"))
    serializer_class = BreedSerializer

class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.annotate(
        breed_avg_age=Subquery(
            Dog.objects.filter(breed=OuterRef("breed"))
            .values("breed")
            .annotate(avg_age=Avg("age"))
            .values("avg_age")
        ),
        same_breed_count=Count("breed__dogs")
    )
     
    serializer_class = DogSerializer

 