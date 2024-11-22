import json, folium, urllib.request
from streamlit_folium import st_folium
import streamlit as st
from folium.features import CustomIcon

weathers = {
        "2": ["뇌우", "#00008b", "⛈"],
        "3": ["이슬비", "#add8e6", "☔"],
        "5": ["비", "#0000ff", "☔"],
        "6": ["눈", "#f5f5f5", "☃"],
        "701": ["안개", "#add8e6", "🌫"], "711": ["짙은 안개", "#bebebe", "🌫"], "721": ["안개", "#bebebe", "🌫"],
        "731": ["황사", "#e9d66b", "😷"], "741": ["안개", "#bebebe", "🌫"], "751": ["황사", "#e9d66b", "😷"],
        "761": ["미세먼지", "#e9d66b", "😷"], "762": ["화산재", "#838b8b", "🌋"],
        "771": ["스콜", "#0000ff", "⛆"], "781": ["토네이도", "#00008b", "🌪"],
        "800": ["맑음", "#318ce7", "☀"], "801": ["구름", "#89cff0", "☁"], "802": ["구름", "#89cff0", "☁"],
        "803": ["흐림", "#7f7f7f", "☁"], "804": ["흐림", "#7f7f7f", "☁"],
    }


def calc_center(loc):
    global coordinates
    geo_average = [0, 0]
    for i in data['features']:
        if i['properties']['adm_nm'] == loc:
            coordinates = i['geometry']
            co_len = len(i['geometry']['coordinates'][0][0])
            for co in i['geometry']['coordinates'][0][0]:
                geo_average[0] += co[0]
                geo_average[1] += co[1]

    geo_average[0] /= co_len
    geo_average[1] /= co_len

    return geo_average[::-1]


def style(location):
    global color
    weather_id = str(get_weather(location[0], location[1])['weather'][0]['id'])
    if weather_id[0] == "7" or weather_id[0] == "8":
        loc_style = {
            'fillColor': weathers[weather_id][1],
            'fillOpacity': 0.7,
            'color': 'black',
            'weight': 1,
            "dashArray": "5, 5"
        }
        color = weathers[weather_id][1]
    else:
        loc_style = {
            'fillColor': weathers[weather_id[0]][1],
            'fillOpacity': 0.7,
            'color': 'black',
            'weight': 1,
            "dashArray": "5, 5"
        }
        color = weathers[weather_id[0]][1]

    return lambda x: loc_style


def get_weather(lat, lon):
    f = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&APPID=c3114ccaa3eada02fe5d90aefc5f249c")
    s = json.loads(f.read())
    return s


with open('Geo_All/Kor.geojson', 'r', encoding='utf-8') as file:
    data = json.load(file)

loc_infos = {}

for _ in data['features']:
    if _['properties']['sidonm'] not in loc_infos.keys():
        loc_infos[_['properties']['sidonm']] = dict()

    if _['properties']['sggnm'] not in loc_infos[_['properties']['sidonm']].keys():
        loc_infos[_['properties']['sidonm']][_['properties']['sggnm']] = []
    loc_infos[_['properties']['sidonm']][_['properties']['sggnm']].append(_['properties']['adm_nm'].split(" ")[-1])

st.set_page_config(page_title="Test_Weather", page_icon="🫠",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🫠전국 날씨 탐색기🫠</h1>', unsafe_allow_html=True)


cols = st.columns(3)
select_loc_si = cols[0].selectbox(label="시/도", options=list(loc_infos.keys()), index=None, key=None)
if select_loc_si is not None:
    select_loc_gun = cols[1].selectbox(label="시/군/구", options=list(loc_infos[select_loc_si].keys()), index=None, key=None)
    if select_loc_si is not None and select_loc_gun is not None:
        select_loc_dong = cols[2].selectbox(label="읍/면/동", options=loc_infos[select_loc_si][select_loc_gun], index=None, key=None)
        if select_loc_dong is not None:
            result_loc = f"{select_loc_si} {select_loc_gun} {select_loc_dong}"
            coo_cen = calc_center(result_loc)
            weather_info = get_weather(coo_cen[0], coo_cen[1])
            weathers_id = str(get_weather(coo_cen[0], coo_cen[1])['weather'][0]['id'])

            mapa = folium.Map(location=coo_cen, zoom_start=14, tiles='cartodbpositron')
            loc = folium.GeoJson(coordinates, style_function=style(coo_cen))
            loc.add_to(mapa)

            st_folium(mapa, width=800, height=450)

            st.markdown(f"""
    <div style="border:2px solid {color}; padding: 10px; border-radius: 10px; background-color: #ffffff;">
        <h2 style="color: {color};">📍{result_loc} 날씨📍</h2>
        <p style="font-size: 18px; color: #000000;">😂 <strong>날씨:</strong> {weathers[weathers_id][0]}</p>
        <p style="font-size: 18px; color: #000000;">🌡️ <strong>기온:</strong> {weather_info['main']['temp']}℃</p>
        <p style="font-size: 18px; color: #000000;">🤒️ <strong>체감기온:</strong> {weather_info['main']['feels_like']}℃</p>
    </div>
""", unsafe_allow_html=True)
