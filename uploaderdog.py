#%%
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
from PIL import Image
from imagesearchandclick import *
import pyautogui
import time
import clipboard
long_wait = 10
short_wait = 3


#####################################################################################################################
######################################### 강아지부분 #################################################################
#####################################################################################################################
#########함수로 한번 만들기 시도해보자.

#%%
driver = webdriver.Chrome('chromedriver.exe')

# 로그인 페이지로 이동
driver.get('https://www.instagram.com/')
driver.maximize_window()
driver.implicitly_wait(long_wait)
# 고양이 계정은 마이스누아이디
# 강아지 계정은 구글부계정연결



# ID와 비밀번호 입력
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('cute_dog_collect')
time.sleep(short_wait)
driver.find_element(
    by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys('zx031263')
time.sleep(short_wait)

# 로그인 버튼 클릭
pyautogui.click(x=1169, y=479)
driver.implicitly_wait(long_wait)
time.sleep(short_wait)
# 만들기 버튼 클릭
searchandclick('make',2)
driver.implicitly_wait(long_wait)
time.sleep(short_wait)
#%%
# 내 파일에서 선택 버튼 클릭
driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
driver.implicitly_wait(long_wait)
time.sleep(short_wait)
#%%

################################## 다이얼로그 컨트롤 부분 #################################

#%%
now = time.localtime()
i = time.strftime('%d', now)
i = i.lstrip('0')  # 앞에 0을 제거
dailycheck = time.strftime('%m월%d일', now)
# 미리 작성한 경로를 클립보드에 복사 ##31일일 분량 한번에 하게되면 날짜별로 다르게 설정해 줘야해
clipboard.copy(f'C:/pythonvscode/instaanimal/dog_image/{i}일')# 복사할 경로를 수정
# 파일 다이얼로그가 특정 위치에 열려있다고 가정
# 파일 다이얼로그가 열리는 시간을 고려하여 충분한 대기 시간을 설정
# 파일 다이얼로그의 경로 입력 창 클릭
pyautogui.click(x=677, y=51)
time.sleep(short_wait)
# 클립보드에 있는 경로 붙여넣기

pyautogui.hotkey('ctrl', 'v')
time.sleep(short_wait)

# 엔터 키 입력
pyautogui.press('enter')
time.sleep(short_wait)
# 파일 목록 로딩을 기다리기 위해 충분한 시간 대기


# 별 의미없음 그냥 파일잇는 곳 아무곳이나 좌표임
pyautogui.click(x=567, y=285)
time.sleep(short_wait)
# 파일 다이얼로그에서 모든 파일 선택 (Ctrl + A)
pyautogui.hotkey('ctrl', 'a')
time.sleep(short_wait)

# 열기 버튼 또는 엔터 키 입력
pyautogui.press('enter')


############################ 다시 인스타 다음 버튼 부터 #################################

#업로드 중 다음 버튼 클릭
driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
driver.implicitly_wait(long_wait)
time.sleep(short_wait)

#한번더 클릭
driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
driver.implicitly_wait(long_wait)
time.sleep(short_wait)


########################## 멘트, 태그 입력 #################################

#멘트와 태그 입력 
driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').click()
driver.implicitly_wait(long_wait)
time.sleep(short_wait)

driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys('cute')
driver.implicitly_wait(long_wait)
time.sleep(short_wait)



##이모티콘 입력
pyautogui.click(x=1163, y=495)
time.sleep(short_wait)
searchandclick('imoji',2)
time.sleep(short_wait)
pyautogui.click(x=1163, y=495)
time.sleep(short_wait)
searchandclick('imoji',2)
time.sleep(short_wait)

##각종 태그 입력

#줄 5번 넘기고 . 으로 표시하기?
driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys('\n.\n.\n.\n.\n.\n')
driver.implicitly_wait(long_wait)
time.sleep(short_wait)

# 태그 리스트
tag_list = ["dogs", "dogsofinstagram", "dog", "pomeranian", "dogstagram", "instagram",
            "doglover", "doglife", "doglovers", "instadog", "puppy", "pets", "puppies",
            "dogoftheday", "love", "cute", "pet", "animals", "cats", "gatos","world",
            "gato", "petsofinstagram", "puppiesofinstagram", "cutedogs", "doglove",
            "adoptdontshop"]  # 태그 리스트에 원하는 태그를 추가

# 문자열과 태그 입력
tag_text = ""
for tag in tag_list:
    tag_text += f"#{tag} "  # 문자열에 태그를 추가

driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys(tag_text)
driver.implicitly_wait(long_wait)
time.sleep(short_wait)
##공유하기 클릭

driver.find_element(
    by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()

time.sleep(long_wait)

driver.quit()


with open("dailylog.txt", "a") as file:
    file.write("\n" + dailycheck + '강아지 업로드 완료')
#%%