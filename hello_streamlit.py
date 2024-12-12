import json

with open('Final/Geo_All/Kor.geojson', 'r', encoding='utf-8') as file:
    data = json.load(file)


loc_infos = {}

for _ in data['features']:
    if _['properties']['sidonm'] not in loc_infos.keys():
        loc_infos[_['properties']['sidonm']] = dict()

    if _['properties']['sggnm'] not in loc_infos[_['properties']['sidonm']].keys():
        loc_infos[_['properties']['sidonm']][_['properties']['sggnm']] = []
    loc_infos[_['properties']['sidonm']][_['properties']['sggnm']].append(_['properties']['adm_nm'].split(" ")[-1])

print(loc_infos)