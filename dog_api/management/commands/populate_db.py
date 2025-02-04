from django.core.management.base import BaseCommand
from faker import Faker
from dog_api.models import Breed, Dog
import random

class Command(BaseCommand):
    """
    Django management-команда для заполнения базы данных случайными данными
    для моделей Breed (порода) и Dog (собака) с использованием библиотеки Faker.
    """
    help = 'Populates the database with random data'

    def handle(self, *args, **kwargs):
        """
        Основной метод, который выполняет команду.
        - Удаляет все существующие записи из таблиц Breed и Dog.
        - Создает предопределенные породы с случайными характеристиками.
        - Добавляет в таблицу Dog 50 случайно сгенерированных собак, привязанных к породам.

        В конце выводит сообщение об успешном заполнении базы данных.
        """
        fake = Faker()
        Faker.seed(0)  

         
        Breed.objects.all().delete()
        Dog.objects.all().delete()

        breed_names = [
            "Labrador", "German", "Golden Retriever", 
            "Bulldog", "Poodle", "Beagle", "Rottweiler", 
            "Yorkshire Terrier", "Dachshund", "Boxer"
        ]
        breeds = []
        for breed_name in breed_names:
            breed = Breed(
                name=breed_name,
                size=random.choice(['small', 'medium', 'large']),
                friendliness=random.randint(1, 5),
                trainability=random.randint(1, 5),
                shedding_amount=random.randint(1, 5),
                exercise_needs=random.randint(1, 5),
            )
            breeds.append(breed)
        Breed.objects.bulk_create(breeds)   

       
        dogs = []
        for _ in range(50):  
            dog = Dog(
                name=fake.first_name(),
                age=random.randint(1, 15),
                breed=random.choice(breeds),   
                gender=random.choice(['male', 'female']),
                color=fake.color_name(),
                favorite_food=fake.word(),
                favorite_toy=fake.word(),
            )
            dogs.append(dog)
        Dog.objects.bulk_create(dogs)   
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))