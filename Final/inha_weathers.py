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


def style(location):
    weather_id = str(get_weather(location[0], location[1])['weather'][0]['id'])
    if weather_id[0] == "7" or weather_id[0] == "8":
        loc_style = {
            'fillColor': weathers[weather_id][1],
            'fillOpacity': 0.7,
            'color': 'black',
            'weight': 1,
            "dashArray": "5, 5"
        }
    else:
        loc_style = {
            'fillColor': weathers[weather_id[0]][1],
            'fillOpacity': 0.7,
            'color': 'black',
            'weight': 1,
            "dashArray": "5, 5"
        }

    return lambda x: loc_style


def calc_center(loc):
    global coordinates
    geo_average = [0, 0]
    for i in data['features']:
        if i['properties']['SIG_KOR_NM'] == loc:
            coordinates = i
            co_len = len(i['geometry']['coordinates'][0])
            for co in i['geometry']['coordinates'][0]:
                geo_average[0] += co[0]
                geo_average[1] += co[1]

    geo_average[0] /= co_len
    geo_average[1] /= co_len

    return geo_average[::-1]


def get_weather(lat, lon):
    f = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&APPID=c3114ccaa3eada02fe5d90aefc5f249c")
    s = json.loads(f.read())
    return s


with open('Final/Geo_All/TL_SCCO_SIG.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

geo_kr_names = [i['properties']['SIG_KOR_NM'] for i in data['features']]
geo_kr_names.sort()

st.set_page_config(page_title="Test_Weather", page_icon="🫠",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})
st.header("🫠전국 날씨 탐색기🫠")
select_loc = st.selectbox(label=":pushpin:을 눌러 날씨를 확인하세요!",options=geo_kr_names, index=None, placeholder="Choose a Location!")

if select_loc is not None:
    coo_cen = calc_center(select_loc)

    weather_info = get_weather(coo_cen[0], coo_cen[1])
    weathers_id = str(get_weather(coo_cen[0], coo_cen[1])['weather'][0]['id'])

    mapa = folium.Map(location=coo_cen, zoom_start=10, tiles='cartodbpositron')
    loc = folium.GeoJson(coordinates, style_function=style(coo_cen))
    loc.add_to(mapa)

    popup = folium.Popup(
        f'''
        <h1 style="color:{weathers[weathers_id][1]}"><strong>{select_loc}</strong> 날씨</h1><h1>{weathers[weathers_id][2]}</h1>
        🌡<strong>온도</strong> : {weather_info["main"]["temp"]} °C<br>
        🌡<strong>체감온도</strong> : {weather_info["main"]["feels_like"]} °C
    ''', max_width=400)

    marker = folium.Marker(location=coo_cen, popup=popup, icon=CustomIcon(
        icon_image="https://cdn-icons-png.flaticon.com/512/4585/4585518.png",
        icon_size=(70, 70)
    ))
    marker.add_to(mapa)
    st_folium(mapa, width=600, height=450)


