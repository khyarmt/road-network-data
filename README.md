# osm-data-downloader

日本国内の道路ネットワークデータを生成するためのスクリプトです。
OpenStreetMap から Shapefile 形式のデータをダウンロードし、道路ネットワークデータを生成します。

## イントロダクション

OpenStreetMap から道路データをダウンロードし、道路ネットワークデータを作成するためのスクリプト。

## ステップ

1. OpenStreetMap からデータのダウンロード（download_shp_files.py）
2. GeoJSON 形式の道路データの作成（shp2json.sh）
3. 道路ネットワークデータの生成
