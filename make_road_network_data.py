import json

geojson_open = open(f'{import_folder}/gis_osm_roads_free_1_{sub_region}.geojson', 'r')
geojson_load = json.load(geojson_open)

road_list = geojson_load['features']
print(road_list[0]['geometry']['coordinates'])
