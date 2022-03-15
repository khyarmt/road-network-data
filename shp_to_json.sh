#!/bin/sh

folder=${1}
sub_region=${2}

shp2json ${folder}/gis_osm_roads_free_1_${sub_region}.shp -o ${folder}/gis_osm_roads_free_1_${sub_region}.geojson
