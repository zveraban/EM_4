from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Breed(models.Model):
    """
    Модель породы собаки.

    Атрибуты:
        name (str): Название породы (до 50 символов).
        size (str): Размер породы, выбирается из доступных вариантов: Tiny, Small, Medium, Large.
        friendliness (int): Уровень дружелюбности (от 1 до 5).
        trainability (int): Уровень обучаемости (от 1 до 5).
        shedding_amount (int): Уровень линьки (от 1 до 5).
        exercise_needs (int): Уровень потребности в физической активности (от 1 до 5).
    """
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
    """
    Модель собаки.

    Атрибуты:
        name (str): Имя собаки (до 50 символов).
        age (int): Возраст собаки (от 0 до 99 лет).
        gender (str): Пол собаки, выбирается из доступных вариантов: Male, Female.
        color (str): Цвет шерсти собаки (до 50 символов).
        favorite_food (str): Любимая еда собаки (до 50 символов).
        favorite_toy (str): Любимая игрушка собаки (до 50 символов).
        breed (ForeignKey): Связь с моделью Breed (порода), каскадное удаление при удалении породы.
    """
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
