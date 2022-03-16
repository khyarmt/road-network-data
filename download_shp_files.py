import datetime
import urllib.request
import zipfile
import subprocess
import os

download_server = 'https://download.geofabrik.de'
region = 'asia'
country = 'japan'

sub_regions = ['hokkaido', 'tohoku', 'kanto', 'chubu', 'kansai', 'chugoku', 'shikoku', 'kyushu']

for sub_region in sub_regions:
    # Make Download Folder
    processing_date = datetime.date.today().strftime('%Y-%m-%d') # スクリプトを実行した日付でフォルダを作成し、この中にデータを格納していく
    if not os.path.exists(processing_date):
        os.makedirs(processing_date)

    # Download Zip
    zip_name = f'{sub_region}-latest-free.shp.zip'
    download_folder = processing_date
    url = f'{download_server}/{region}/{country}/{zip_name}'
    urllib.request.urlretrieve(url, f'{download_folder}/{zip_name}')

    # Unzip Data
    with zipfile.ZipFile(f'{download_folder}/{zip_name}') as zf:
        extension_list = ['cpg', 'dbf', 'prj', 'shp', 'shx']
        for extension in extension_list:
            zf.extract(f'gis_osm_roads_free_1.{extension}', f'{download_folder}')
            os.rename(f'{download_folder}/gis_osm_roads_free_1.{extension}', f'{download_folder}/gis_osm_roads_free_1_{sub_region}.{extension}')

    # Deliete Unnecessary Files
    os.remove(f'{download_folder}/{zip_name}')
