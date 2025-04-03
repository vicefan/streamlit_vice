import base64
import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


st.set_page_config(page_title="viceversartist", page_icon="🫠",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})

st.title('나이스지키미 로그인 시키지마라')
os.system("chmod +r ./sec_x.crx")

st.text(st.secrets['pw'])

def get_driver():
    options = webdriver.ChromeOptions()

    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_extension("./sec_x.crx")

    service = Service()

    return webdriver.Chrome(service=service, options=options)


def get_screenshot(app_url):
    driver = get_driver()
    driver.get(app_url)

    time.sleep(3)

    # Explicitly wait for an essential element to ensure content is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    myid = driver.find_element(By.XPATH, '//*[@id="userId"]')
    myid.send_keys(st.secrets['id'])
    mypw = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    mypw.send_keys(st.secrets['pw'])
    mybtn = driver.find_element(By.XPATH, '//*[@id="idLoginBtn"]')
    mybtn.click()

    time.sleep(5)

    count = driver.find_element(By.XPATH, '//*[@id="capture"]/div[2]/a[1]/strong')
    st.code(driver.page_source)
    return count.text


with st.form("my_form"):
    fam_name = st.text_input("성")
    given_name = st.text_input("이름")
    raw_str = f"{fam_name}{given_name},1,{given_name},{fam_name},Y"
    encoded_str = base64.b64encode(raw_str.encode()).decode()
    app_url = f"https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20?param={encoded_str}&uaCheck=Y"
    submitted = st.form_submit_button("Submit")
    if submitted:
        if app_url:
            count = get_screenshot(app_url)
            st.subheader("Count:", count)