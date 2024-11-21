# This Python file uses the following encoding: utf-8
import urllib.request, json, folium
import geopandas as gpd
from folium.features import CustomIcon
from streamlit_folium import st_folium
import streamlit as st

st.set_page_config(page_title="INHA_WEATHERS", page_icon="🫠", layout="wide",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})
st.header("🫠인하대학교 주변 날씨🫠")
st.write("🌡️온도는 ℃로 표시됩니다.")
st.write("👉🏼이모지를 눌러 날씨 정보를 확인하세요.")
c_box = st.checkbox("✅날씨 정보 보기")

if c_box:
    locations = {
        "dohwa": ["Final/Geo_Split/dohwa.geojson", (37.469248, 126.660751)],
        "ganseok": ["Final/Geo_Split/ganseok.geojson", (37.461129, 126.703504)],
        "guwol": ["Final/Geo_Split/guwol.geojson", (37.447230, 126.706705)],
        "gwankyo": ["Final/Geo_Split/gwankyo.geojson", (37.440732, 126.686613)],
        "hakik": ["Final/Geo_Split/hakik.geojson", (37.434989, 126.649610)],
        "juan": ["Final/Geo_Split/juan.geojson", (37.457082, 126.677223)],
        "sunge": ["Final/Geo_Split/sunge.geojson", (37.461215, 126.645630)],
        "yonghyun": ["Final/Geo_Split/yonghyun.geojson", (37.451925, 126.647227)],
        }

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


    def get_weather(lat, lon):
        f = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&APPID=c3114ccaa3eada02fe5d90aefc5f249c")
        s = json.loads(f.read())
        return s


    def style(location):
        weather_id = str(weather_info[location]['weather'][0]['id'])
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

    def get_icon(loc):
        anchor = {
            "dohwa": (10, 50),
            "ganseok": (10, 50),
            "guwol": (10, 50),
            "sunge": (10, 50),
            "yonghyun": (30, 45),
            "juan": (10, 20),
            "gwankyo": (-30, 30),
            "hakik": (0, 80),
        }

        icon = CustomIcon(
            icon_image=f"https://openweathermap.org/img/wn/{weather_info[loc]['weather'][0]['icon']}@2x.png",
            icon_size=(70, 70) if loc != "gwankyo" else (40, 40),
            icon_anchor=anchor[loc],
        )

        return icon

    def gpd_naming(x):
        return gpd.read_file(locations[x][0])


    dohwa = gpd_naming("dohwa")
    ganseok = gpd_naming("ganseok")
    guwol = gpd_naming("guwol")
    gwankyo = gpd_naming("gwankyo")
    hakik = gpd_naming("hakik")
    juan = gpd_naming("juan")
    sunge = gpd_naming("sunge")
    yonghyun = gpd_naming("yonghyun")

    weather_info = {name: get_weather(lat, lon) for name, (path, (lat, lon)) in locations.items()}

    emoji_dohwa, color_dohwa = weathers[str(weather_info["dohwa"]['weather'][0]['id'])][2], weathers[str(weather_info["dohwa"]['weather'][0]['id'])][1]
    emoji_ganseok, color_ganseok = weathers[str(weather_info["ganseok"]['weather'][0]['id'])][2], weathers[str(weather_info["ganseok"]['weather'][0]['id'])][1]
    emoji_guwol, color_guwol = weathers[str(weather_info["guwol"]['weather'][0]['id'])][2], weathers[str(weather_info["guwol"]['weather'][0]['id'])][1]
    emoji_gwankyo, color_gwankyo = weathers[str(weather_info["gwankyo"]['weather'][0]['id'])][2], weathers[str(weather_info["gwankyo"]['weather'][0]['id'])][1]
    emoji_hakik, color_hakik = weathers[str(weather_info["hakik"]['weather'][0]['id'])][2], weathers[str(weather_info["hakik"]['weather'][0]['id'])][1]
    emoji_juan, color_juan = weathers[str(weather_info["juan"]['weather'][0]['id'])][2], weathers[str(weather_info["juan"]['weather'][0]['id'])][1]
    emoji_sunge, color_sunge = weathers[str(weather_info["sunge"]['weather'][0]['id'])][2], weathers[str(weather_info["sunge"]['weather'][0]['id'])][1]
    emoji_yonghyun, color_yonghyun = weathers[str(weather_info["yonghyun"]['weather'][0]['id'])][2], weathers[str(weather_info["yonghyun"]['weather'][0]['id'])][1]

    popup_dohwa = folium.Popup(
        f'''
        <h1 style="color:{color_dohwa}"><strong>도화동</strong> 날씨</h1><h1>{emoji_dohwa}</h1>
        <strong>온도</strong> : {weather_info["dohwa"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["dohwa"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_ganseok = folium.Popup(
        f'''
        <h1 style="color:{color_ganseok}"><strong>간석동</strong> 날씨</h1><h1>{emoji_ganseok}</h1>
        <strong>온도</strong> : {weather_info["ganseok"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["ganseok"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_guwol = folium.Popup(
        f'''
        <h1 style="color:{color_guwol}"><strong>구월동</strong> 날씨</h1><h1>{emoji_guwol}</h1>
        <strong>온도</strong> : {weather_info["guwol"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["guwol"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_gwankyo = folium.Popup(
        f'''
        <h1 style="color:{color_gwankyo}"><strong>관교동</strong> 날씨</h1><h1>{emoji_gwankyo}</h1>
        <strong>온도</strong> : {weather_info["gwankyo"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["gwankyo"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_hakik = folium.Popup(
        f'''
        <h1 style="color:{color_hakik}"><strong>학익동</strong> 날씨</h1><h1>{emoji_hakik}</h1>
        <strong>온도</strong> : {weather_info["hakik"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["hakik"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_juan = folium.Popup(
        f'''
        <h1 style="color:{color_juan}"><strong>주안동</strong> 날씨</h1><h1>{emoji_juan}</h1>
        <strong>온도</strong> : {weather_info["juan"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["juan"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_sunge = folium.Popup(
        f'''
        <h1 style="color:{color_sunge}"><strong>숭의동</strong> 날씨</h1><h1>{emoji_sunge}</h1>
        <strong>온도</strong> : {weather_info["sunge"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["sunge"]["main"]["feels_like"]} °C
    ''', max_width=400)

    popup_yonghyun = folium.Popup(
        f'''
        <h1 style="color:{color_yonghyun}"><strong>용현동</strong> 날씨</h1><h1>{emoji_yonghyun}</h1>
        <strong>온도</strong> : {weather_info["yonghyun"]["main"]["temp"]} °C<br>
        <strong>체감온도</strong> : {weather_info["yonghyun"]["main"]["feels_like"]} °C
    ''', max_width=400)

    mapa = folium.Map(location=(37.45, 126.68), zoom_start=13, tiles='Cartodb Positron')
    g_dohwa = folium.GeoJson(dohwa, name="도화", style_function=style("dohwa")).add_to(mapa)
    folium.Marker(location=locations["dohwa"][1], popup=popup_dohwa, icon=get_icon("dohwa")).add_to(mapa)
    g_ganseok = folium.GeoJson(ganseok, name="간석", style_function=style("ganseok")).add_to(mapa)
    folium.Marker(location=locations["ganseok"][1], popup=popup_ganseok, icon=get_icon("ganseok")).add_to(mapa)
    g_guwol = folium.GeoJson(guwol, name="구월", style_function=style("guwol")).add_to(mapa)
    folium.Marker(location=locations["guwol"][1], popup=popup_guwol, icon=get_icon("guwol")).add_to(mapa)
    g_gwankyo = folium.GeoJson(gwankyo, name="관교", style_function=style("gwankyo")).add_to(mapa)
    folium.Marker(location=locations["gwankyo"][1], popup=popup_gwankyo, icon=get_icon("gwankyo")).add_to(mapa)
    g_hakik = folium.GeoJson(hakik, name="학익", style_function=style("hakik")).add_to(mapa)
    folium.Marker(location=locations["hakik"][1], popup=popup_hakik, icon=get_icon("hakik")).add_to(mapa)
    g_juan = folium.GeoJson(juan, name="주안", style_function=style("juan")).add_to(mapa)
    folium.Marker(location=locations["juan"][1], popup=popup_juan, icon=get_icon("juan")).add_to(mapa)
    g_sunge = folium.GeoJson(sunge, name="숭의", style_function=style("sunge")).add_to(mapa)
    folium.Marker(location=locations["sunge"][1], popup=popup_sunge, icon=get_icon("sunge")).add_to(mapa)
    g_yonghyun = folium.GeoJson(yonghyun, name="용현", style_function=style("yonghyun")).add_to(mapa)
    folium.Marker(location=locations["yonghyun"][1], popup=popup_yonghyun, icon=get_icon("yonghyun")).add_to(mapa)

    st_folium(mapa, width=1400, height=600, center=(37.45, 126.68), zoom=13)