import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(excutable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.credit.co.kr/ib20/mnu/BZWMNLGNM20?param=67CV67CV7J20LDEs67CV7J20LOuwlSxZ&uaCheck=Y")

myid = driver.find_element(By.XPATH, '//*[@id="userId"]')
myid.send_keys("dddooong2000")
mypw = driver.find_element(By.XPATH, '//*[@id="pwd"]')
mypw.send_keys("Chan0thug!")
mybtn = driver.find_element(By.XPATH, '//*[@id="idLoginBtn"]')
mybtn.click()

time.sleep(10)