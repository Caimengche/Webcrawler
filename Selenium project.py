from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open chrome driver with selenium
s = Service("C:/Users/USER/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service = s)
#用driver進入網站
driver.get("https://www.google.com.tw/?hl=zh_TW")
search = driver.find_element("name", "q")
search.send_keys("黑毓芳")
search.send_keys(Keys.RETURN)

#等網頁跳轉出現特定的標籤之後再繼續執行 explicit wait 寫法 數字是最長可以等待的時間
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hdtb-msel")))
#找到tag name 印出該元素的文字
titles = driver.find_elements("tag name","h3")
for title in titles:
    print(title.text)


time.sleep(5)
driver.quit()

#取得網頁標籤

