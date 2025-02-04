from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Breed(models.Model):
    SIZE_CHOICES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Введите значение от 1 до 5"
    )
    trainability = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Введите значение от 1 до 5"
    )
    shedding_amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Введите значение от 1 до 5"
    )
    exercise_needs = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Введите значение от 1 до 5"
    )

class Dog(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        help_text="Введите возраст от 0 до 99"
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    color  = models.CharField(max_length=50)
    favorite_food  = models.CharField(max_length=50)
    favorite_toy   = models.CharField(max_length=50)
    breed = models.ForeignKey(Breed, related_name="dogs", on_delete=models.CASCADE)
