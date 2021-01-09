from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(12)

    price = browser.find_element_by_xpath("//h5[@id='price' and text()='$100']")
    btn = browser.find_element_by_css_selector("button[id='book']")
    btn.click()
    
    x = browser.find_element_by_css_selector("span[id='input_value']")
    x = str(math.log(abs(12 * math.sin(int(x.text)))))

    answer = browser.find_element_by_css_selector("input[id='answer']")
    answer.send_keys(x)

    send = browser.find_element_by_css_selector("button[id='solve']")
    send.click()
    
finally:
    time.sleep(50)
    browser.quit()