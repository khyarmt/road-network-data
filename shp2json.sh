#!/bin/sh

processing_date=${1}

mkdir -p ${processing_date}/geojson
for sub_region in "hokkaido" "tohoku" "kanto" "chubu" "kansai" "chugoku" "shikoku" "kyushu"; do
    shp2json --encoding utf-8 ${processing_date}/shapefile/gis_osm_roads_free_1_${sub_region}.shp -o ${processing_date}/geojson/gis_osm_roads_free_1_${sub_region}.geojson
done
