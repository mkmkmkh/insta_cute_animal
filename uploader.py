import os
import urllib
import unicodedata
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import * 
from PIL import Image


watingtime = 10

driver = webdriver.Chrome('chromedriver.exe')

# 로그인 페이지로 이동
driver.get('https://www.instagram.com/login/')

# ID와 비밀번호 입력
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('noryangbob')
time.sleep(1)

driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('zx031263')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
driver.implicitly_wait(watingtime)

# 업로드 페이지로 이동
driver.get('<https://www.instagram.com/create/>')

# 파일 선택
upload_input = driver.find_element_by_xpath('//input[@type="file"]')

# 파일 대화상자 열기
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(initialdir=filepath, title="Select a File", filetypes=(("Video files", "*.mp4;*.avi"), ("All files", "*.*")))
upload_input.send_keys(file_path)

# 캡션과 위치 정보 입력
caption_input = driver.find_element_by_xpath('//textarea[@aria-label="캡션 추가"]')
caption_input.send_keys(caption)

location_input = driver.find_element_by_xpath('//input[@aria-label="위치 추가"]')
location_input.send_keys(location)

# 게시글 업로드
share_button = driver.find_element_by_xpath('//button[@type="submit"]')
share_button.click()

# 10초 대기 후 브라우저 닫기
time.sleep(10)
driver.quit()

#%%
