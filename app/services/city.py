import folium
import osmnx as ox

from app.log import logger
from config import TAGS


def get_objects(city: str, tags: dict) -> dict:
    """
    Получает объекты (POI) по заданным категориям
    для указанного города с помощью OSMnx.

    Args:
        city (str): Название города (например, "Moscow").
        tags (dict): Словарь тегов для поиска.
    
    Returns:
        dict: Вложенный словарь с найденными объектами OSM.

    Raises:
        osmnx._errors.InsufficientResponseError:
            Возникает, если Overpass API не вернул данные по указанным тегам.
            Обрабатывается внутри функции — только логгируется предупреждение.
    """
    city_objects = {}
    
    for tag_category, tag_values in tags.items():
        city_objects[tag_category] = {}

        for tag_value in tag_values:
            single_tag_filter = {tag_category: tag_value}
            
            try:
                geo_objects = ox.features.features_from_place(
                    buffer_dist=None,
                    query=city,
                    tags=single_tag_filter,
                    which_result=None)

                if geo_objects is not None and not geo_objects.empty:
                    city_objects[tag_category][tag_value] = geo_objects
            except ox._errors.InsufficientResponseError:
                logger.warning(f"Нет данных для {city}: {tag_category}={tag_value}")

    return city_objects


def fetch_city_data(city_en, city_ru):
    """
    Получает границы города, преобразует их
    в GeoJSON и собирает объекты (POI).

    Args:
        city_en (str): Название города на английском (например, "Moscow").
        city_ru (str): Название города на русском (например, "Москва").

    Returns:
        tuple:
            - str: Название города на русском
            - folium.GeoJson: GeoJSON-объект с границей города
            - dict: Результат функции get_objects — все найденные объекты по тегам

    Raises:
        osmnx._errors.GeocoderError:
            Если не удалось получить геометрию города через `geocode_to_gdf`.
    """
    city_gdf = ox.geocode_to_gdf(city_en)
    geojson = city_gdf.to_json()
    geojson_layer = folium.GeoJson(
        geojson,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.2,
        name=city_en,
        weight=2,
    )
    city_objects = get_objects(city_en, TAGS)
    return city_ru, geojson_layer, city_objects
