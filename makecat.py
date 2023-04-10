#%%
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import pyautogui 
import cv2
import numpy as np
import pyperclip
import urllib
#%%
#import sys
#sys.path.append("C:/pythonvscode/instaanimal")  # 모듈이 있는 디렉토리의 절대 경로를 추가
from imagesearchandclick import *

# 이미지 매칭 함수 정의
def find_template(template, threshold=0.8):
    screenshot = cv2.imread('screenshot.png', 0)
    template = cv2.imread(template, 0)
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    if len(loc[0]) > 0:
        found_x = int(loc[1][0] + template.shape[1] / 2)
        found_y = int(loc[0][0] + template.shape[0] / 2)
        return found_x, found_y
    else:
        return None

#waiting time
input_wait_time = 3
im_wait_time = 7

###############크롬로그인################################

# 크롬드라이버 옵션 설정
# undetected_chromedriver를 사용하여 크롬드라이버 인스턴스 생성
driver = uc.Chrome( version_main = 111)
# 웹 브라우저 조작 코드 작성
driver.get('https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync')
driver.maximize_window()
driver.implicitly_wait(im_wait_time)
#로그인 인풋 클릭
pyautogui.click(x=882, y=531)
time.sleep(input_wait_time)
pyautogui.typewrite('k1992ny')
time.sleep(input_wait_time)
pyautogui.click(x=1100, y=730)
driver.implicitly_wait(im_wait_time)
#비밀번호 인풋 클릭
pyautogui.click(x=886, y=547)
time.sleep(input_wait_time)
pyautogui.typewrite('eojin-0312')
time.sleep(input_wait_time)
pyautogui.click(x=1100, y=665)
time.sleep(input_wait_time)

driver.get('https://playgroundai.com/create')
driver.implicitly_wait(im_wait_time)

pyautogui.click(x=1200, y=633)
time.sleep(im_wait_time)
driver.implicitly_wait(im_wait_time)
####################################### 프롬프트 붙여넣기 #################################
#%%
pyautogui.click(x=180, y=480)
time.sleep(im_wait_time)
##prompt 파일 불러와서 붙여넣기
# 텍스트 파일 읽기
with open('./prompt/cat_prompt.txt', 'r') as f:
    text = f.read()
# 텍스트를 클립보드에 복사
pyperclip.copy(text)
# 클립보드 내용 붙여넣기
pyautogui.hotkey('ctrl', 'v')  # Ctrl + V 키 입력
time.sleep(input_wait_time)
#except단어 클릭
pyautogui.click(x=347, y=776)
time.sleep(input_wait_time)
##prompt_remove 파일 불러와서 붙여넣기
with open('./prompt/cat_remove_prompt.txt', 'r') as f:
    text = f.read()
# 텍스트를 클립보드에 복사
pyperclip.copy(text)
# 클립보드 내용 붙여넣기
pyautogui.hotkey('ctrl', 'v')  # Ctrl + V 키 입력
#%%
################################ 모델선택, 파라미터 입력################################

pyautogui.click(x=1660, y=261)
time.sleep(input_wait_time)
pyautogui.click(x=1660, y=339)
time.sleep(input_wait_time)

pyautogui.click(x=1868, y=576)
time.sleep(input_wait_time)
##ctrl a, backspace, 6 순차적입력
pyautogui.hotkey('ctrl', 'a')
time.sleep(input_wait_time)
# Backspace 입력
pyautogui.press('backspace')
time.sleep(input_wait_time)
# 숫자 6 입력
pyautogui.press('6')
time.sleep(input_wait_time)
pyautogui.press('enter')
time.sleep(input_wait_time)

##
pyautogui.click(x=1868, y=718)
time.sleep(input_wait_time)
##ctrl a, backspace, 50 순차적입력
pyautogui.hotkey('ctrl', 'a')
time.sleep(input_wait_time)
# Backspace 입력
pyautogui.press('backspace')
time.sleep(input_wait_time)
# 숫자 6 입력
pyautogui.press('5')
pyautogui.press('0')
time.sleep(input_wait_time)
pyautogui.press('enter')
time.sleep(input_wait_time)
#마우스 휠다운 하자
scroll_amount = -1000  # 스크롤 다운 정도 (음수 값일 경우 스크롤 다운)
pyautogui.scroll(scroll_amount)
time.sleep(input_wait_time)
pyautogui.click(x=1850, y=786)
time.sleep(input_wait_time)

#%% 사진 20개 만들기~
#generate 클릭.
for i in range(5):
    pyautogui.click(x=200, y=1000)
    time.sleep(im_wait_time*2)
    pyautogui.press('esc')
    time.sleep(input_wait_time)

#%%

images = driver.find_elements(
    by=By.CSS_SELECTOR, value='img.rounded-md.object-contain')
img_url = []
time.sleep(0.5)
driver.implicitly_wait(im_wait_time)
# img_url = images.__getattribute__('src')

for image in images:
    url = image.get_attribute('src')
    img_url.append(url)
    
time.sleep(0.5)
driver.implicitly_wait(im_wait_time)
folder_path = 'cat_image'

for i in range(len(img_url)):
    file_path = os.path.join(folder_path, f'cat_{i}.jpg')  # cat_image 폴더 안에 파일 경로 지정
    urllib.request.urlretrieve(img_url[i], file_path)
    time.sleep(0.5)


#%%


folder_path = 'cat_image'

# 이번달 폴더의 경로 가져오기
now = time.localtime()
this_month_folder_name = time.strftime('%m', now)
this_month_folder_path = os.path.join(folder_path, this_month_folder_name)

# 이번달 - 1 폴더부터 이번달 - 31 폴더까지 생성하고 이미지 다운로드
for i in range(1, 32):
    # 이번달 - i 폴더 생성
    this_month_day_folder_name = time.strftime('%d', time.localtime(time.mktime(now) - 86400 * i))
    this_month_day_folder_path = os.path.join(this_month_folder_path, this_month_day_folder_name)
    os.makedirs(this_month_day_folder_path, exist_ok=True)
    
    # img_url 리스트에 있는 이미지를 다운로드하여 이번달 - i 폴더에 저장
    for j in range(len(img_url)):
        # 파일 이름을 cat_{폴더번호}_{이미지번호}.jpg 로 설정
        file_name = f'cat_{i}_{j}.jpg'
        file_path = os.path.join(this_month_day_folder_path, file_name)
        urllib.request.urlretrieve(img_url[j], file_path)
        time.sleep(0.5)



