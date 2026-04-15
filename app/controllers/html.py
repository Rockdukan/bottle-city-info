from concurrent.futures import ThreadPoolExecutor, as_completed

import folium
# import geopandas as gpd
# import osmnx as ox
from bottle import template

from app import app
from app.services import city
from config import CITIES, LOCATION, TAGS, ZOOM


@app.route("/")
def index():
    folium_map = folium.Map(location=LOCATION, zoom_start=ZOOM)
    city_data = {}

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(city.fetch_city_data, city_en, city_ru)
            for city_en, city_ru in CITIES.items()
        ]

        for future in as_completed(futures):
            city_ru, geojson_layer, objects = future.result()
            geojson_layer.add_to(folium_map)
            city_data[city_ru] = objects

    folium_map = folium_map._repr_html_()
    return template("index", city_data=city_data, map=folium_map, tags=TAGS)
