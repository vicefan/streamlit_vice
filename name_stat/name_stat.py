import base64
import streamlit as st
import time
import random
import os
from PIL import Image, ImageDraw, ImageOps
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from os.path import exists


st.set_page_config(page_title="viceversartist", page_icon="🫠",
                   menu_items={"About": "www.instagram.com/rollingloud/viceversartist"})

st.title('나이스지키미 로그인 시키지마라')

def get_driver():
    options = webdriver.ChromeOptions()

    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument(f"--window-size={1920}x{1080}")

    service = Service()

    return webdriver.Chrome(service=service, options=options)


def get_screenshot(app_url):
    driver = get_driver()
    if app_url.endswith('streamlit.app'):
        driver.get(f"{app_url}/~/+/")
    else:
        driver.get(app_url)
    st.text(f"URL: {app_url}")

    time.sleep(3)

    # Explicitly wait for an essential element to ensure content is loaded
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    myid = driver.find_element(By.XPATH, '//*[@id="userId"]')
    myid.send_keys("dddooong2000")
    mypw = driver.find_element(By.XPATH, '//*[@id="pwd"]')
    mypw.send_keys("Chan0thug!")
    mybtn = driver.find_element(By.XPATH, '//*[@id="idLoginBtn"]')
    mybtn.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    time.sleep(10)


    # Get scroll height and width
    # scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    # scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')

    # Set window size
    # driver.set_window_size(scroll_width, scroll_height)

    # Now, capture the screenshot
    driver.save_screenshot('screenshot.png')


def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)

    alpha = Image.new('L', im.size, 255)
    w, h = im.size

    # Apply rounded corners only to the top
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))

    im.putalpha(alpha)
    return im


def generate_app_image():
    bg_random = random.randint(1, 100)
    if bg_random < 10:
        bg_random = '0' + str(bg_random)
    bg_img = Image.open(f'background/background-{bg_random}.jpeg')
    app_img = Image.open('screenshot.png')

    # Create a blank white rectangle
    w, h = app_img.width, app_img.height
    img = Image.new('RGB', (w, h), color='white')

    # Create a drawing object
    draw = ImageDraw.Draw(img)

    # Define the coordinates of the rectangle (left, top, right, bottom)
    rectangle_coordinates = [(0, 0), (w + 50, h + 0)]

    # Draw the white rectangle
    draw.rectangle(rectangle_coordinates, fill='#FFFFFF')
    img = add_corners(img, 24)
    img.save('rect.png')
    ###
    # Resize app image
    image_resize = 0.5  # Increase this value to make the image larger
    new_width = int(img.width * image_resize)
    new_height = int(img.height * image_resize)
    resized_app_img = app_img.resize((new_width, new_height))

    # Crop top portion of app_img
    border = (0, 4, 0, 0)  # left, top, right, bottom
    resized_app_img = ImageOps.crop(resized_app_img, border)

    # Add corners
    resized_app_img = add_corners(resized_app_img, 24)

    img.paste(resized_app_img, (int(resized_app_img.width * 0.025), int(resized_app_img.width * 0.035)),
              resized_app_img)
    img.save('app_rect.png')

    ###
    # Resize app image
    image_resize_2 = 0.5  # Increase this value to make the image larger
    new_width_2 = int(bg_img.width * image_resize_2)
    new_height_2 = int(bg_img.height * image_resize_2)
    resized_img = img.resize((new_width_2, new_height_2))

    bg_img.paste(resized_img, (int(bg_img.width * 0.05), int(bg_img.width * 0.06)), resized_img)
    # bg_img.save('final.png')

    st.image(bg_img)


# Input URL
with st.form("my_form"):
    fam_name = st.text_input("성")
    given_name = st.text_input("이름")
    raw_str = f"{fam_name}{given_name},1,{given_name},{fam_name},Y"
    encoded_str = base64.b64encode(raw_str.encode()).decode()
    app_url = f"https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20?param={encoded_str}&uaCheck=Y"
    # app_url = st.text_input('App URL', 'https://langchain-quickstart.streamlit.app').rstrip('/')
    app_name = app_url.replace('https://', '').replace('.streamlit.app', '')

    submitted = st.form_submit_button("Submit")
    if submitted:
        if app_url:
            get_screenshot(app_url)

file_exists = exists('screenshot.png')
if file_exists:
    generate_app_image()