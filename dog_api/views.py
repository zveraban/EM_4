from rest_framework import viewsets
from django.db.models import Avg, Count, Subquery, OuterRef
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

class BreedViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели породы (Breed).

    Доступные действия:
        - list: Получение списка пород.
        - retrieve: Получение информации о конкретной породе.
        - create: Создание новой породы.
        - update: Обновление информации о породе.
        - partial_update: Частичное обновление информации.
        - destroy: Удаление породы.

    Аннотации:
        - dog_count (int): Количество собак данной породы.
    """
    queryset = Breed.objects.annotate(dog_count=Count("dogs"))
    serializer_class = BreedSerializer

class DogViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели собаки (Dog).

    Доступные действия:
        - list: Получение списка собак.
        - retrieve: Получение информации о конкретной собаке.
        - create: Создание новой собаки.
        - update: Обновление информации о собаке.
        - partial_update: Частичное обновление информации.
        - destroy: Удаление собаки.

    Аннотации:
        - breed_avg_age (float): Средний возраст собак данной породы.
        - same_breed_count (int): Количество собак той же породы.
    """
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

 