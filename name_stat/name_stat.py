import base64
import streamlit as st


st.set_page_config(page_title="viceversartist", page_icon="🫠",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})

st.title("나이스지키미 로그인 시키지마라")
cols = st.columns(2)
with cols[0]:
    st.subheader("이름을 적어주세요.")
    fam_name = st.text_input("성")
    given_name = st.text_input("이름")
    raw_str = f"{fam_name}{given_name},1,{given_name},{fam_name},Y"
    encoded_str = base64.b64encode(raw_str.encode()).decode()
    link = f"https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20?param={encoded_str}&uaCheck=Y"
