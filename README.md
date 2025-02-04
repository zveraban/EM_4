# DogList
DogList - API Веб-приложение для добавления и хранения собак по породам, с возможность полчения информации о среднем возрасте собак по породам и количества собак одной породы 

![Django](https://img.shields.io/badge/Django-5.1.5-green)
![DRF](https://img.shields.io/badge/DRF-3.15.2-blue)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Gunicorn](https://img.shields.io/badge/Gunicorn-23.0.0-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
[![Faker](https://img.shields.io/badge/Faker-35.2.0-blue)](https://pypi.org/project/Faker/)
![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=flat&logo=docker)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg?style=flat&logo=postgresql)](https://www.postgresql.org/)

## 1. Основные функции
Документация Swagger доступна по адресу api/docs/
### Породы собак
 1. Полчение списка всех пород, метод GET /api/breeds/
 2. Добавление породы, метод POST /api/breeds/
 3. Полчение породы по id,  метод GET /api/breeds/{id}/
 4. Обновлении информации о породе, метод PUT /api/breeds/{id}/
 5. Частичное обновление информации о породе, метод PATCH /api/breeds/{id}/
 6. Удаление породы, метод DELETE /api/breeds/{id}/

### Собаки 
 1. Полчение списка всех собак, метод GET /api/dogs/
 2. Добавление собаки, метод POST /api/dogs/
 3. Полчение собаки по id,  метод GET /api/dogs/{id}/
 4. Обновлении информации о собаке, метод PUT /api/dogs/{id}/
 5. Частичное обновление информации о собаке, метод PATCH /api/dogs/{id}/
 6. Удаление собаки, метод DELETE /api/breeds/{id}/

## 2. Установка и запуск
С использованием Docker
1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/zveraban/EM_4.git
2. Проверьте версию Docker и Docker Compose, либо установите:
    ```bash
    docker --version
    docker-compose --version
3. Создайте файл .env  с переменными окружения (пример: .env.example)
    ```bash
    
    SECRET_KEY='django-insecure'
    DEBUG=True
    ALLOWED_HOSTS = 'localhost 127.0.0.1 0.0.0.0'
    
    # Параметры подключения к базе данных
    NAME = dog_db
    USER = postgres
    PASSWORD = postgres
    HOST = db
    PORT = 5432
4. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build

## 3. Пример использования 
    1. Полyчение информации о всех породах
    [
        {
            "id": 5,
            "dog_count": 7,
            "name": "Poodle",
            "size": "large",
            "friendliness": 4,
            "trainability": 5,
            "shedding_amount": 5,
            "exercise_needs": 4
        },
        {
            "id": 4,
            "dog_count": 2,
            "name": "Bulldog",
            "size": "medium",
            "friendliness": 3,
            "trainability": 3,
            "shedding_amount": 1,
            "exercise_needs": 4
        }
    ]

    2. Получение информации о всех собаках
    [
        {
            "id": 87,
            "breed_name": "Yorkshire Terrier",
            "same_breed_count": 5,
            "breed_avg_age": 6.2,
            "name": "Melissa",
            "age": 15,
            "gender": "female",
            "color": "Indigo",
            "favorite_food": "answer",
            "favorite_toy": "technology",
            "breed": 19
        },
        {
            "id": 71,
            "breed_name": "Labrador",
            "same_breed_count": 5,
            "breed_avg_age": 7.4,
            "name": "Carrie",
            "age": 10,
            "gender": "male",
            "color": "LightSlateGray",
            "favorite_food": "light",
            "favorite_toy": "benefit",
            "breed": 12
        }
    ]