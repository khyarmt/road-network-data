import urllib.request
import os
import zipfile
import datetime
import subprocess

download_server = 'https://download.geofabrik.de'
region = 'asia'
country = 'japan'
#sub_regions = ['hokkaido', 'tohoku', 'kanto', 'chubu', 'kansai', 'chugoku', 'shikoku', 'kyushu']
sub_regions = ['shikoku']

# Make Download Folder
download_folder = datetime.date.today().strftime('%Y-%m-%d')
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for sub_region in sub_regions:
    # Download Zip
    folder = f'{sub_region}-latest-free.shp.zip'
    url = f'{download_server}/{region}/{country}/{folder}'
    urllib.request.urlretrieve(url, f'{download_folder}/{folder}')

    # Unzip Data
    with zipfile.ZipFile(f'{download_folder}/{folder}') as zf:
        zf.extract('gis_osm_roads_free_1.shp', f'{download_folder}')

    os.rename(f'{download_folder}/gis_osm_roads_free_1.shp', f'{download_folder}/gis_osm_roads_free_1_{sub_region}.shp')

    # Change .shp to .geojson
    subprocess.run(['sh', 'shp2json.sh', download_folder, sub_region], stdout = subprocess.PIPE, shell = False)

    # Deliete Unnecessary Files
    os.remove(f'{download_folder}/{sub_region}-latest-free.shp.zip')
    os.remove(f'{download_folder}/gis_osm_roads_free_1_{sub_region}.shp')
