import logging
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "app.log")
LOG_LEVEL = logging.INFO
LOG_BACKUP_DAYS = 7
LOG_CONSOLE = True
LOG_CONSOLE_COLOR = True

TEMPLATE_DIR = os.path.join(BASE_DIR, "app", "views")

HOST = "127.0.0.1"
PORT = 8080
DEBUG = True
RELOADER = True


# Координаты центра карты
LOCATION = [45.0234, 41.5824]

# Начальный масштаб
ZOOM = 6


CITIES = {
    "Astrakhan": "Астрахань",
    "Vladikavkaz": "Владикавказ",
    "Volgograd": "Волгоград",
    "Grozny": "Грозный",
    "Krasnodar": "Краснодар",
    "Rostov-on-Don": "Ростов-на-Дону",
}

# Теги OSM по категориям
TAGS = {
    "amenity": {
        "cinema": "Кинотеатры",
        "community_centre": "Места проведения мероприятий",
        "library": "Библиотеки"
    },
    "leisure": {
        "park": "Парки",
        "sports_centre": "Спортивные центры",
        "sports_hall": "Спортивные залы",
        "stadium": "Стадионы",
        "swimming_pool": "Бассейны",
        "water_park": "Аквапарки"
    },
    "natural": {
        "beach": "Пляжи"
    },
    "tourism": {
        "theme_park": "Парки развлечений"
    }
}
