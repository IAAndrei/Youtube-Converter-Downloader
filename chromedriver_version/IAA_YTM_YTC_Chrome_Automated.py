from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

LNKINPUT = input("Enter video url: ")

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://ytmp3.cc/en13/")

inputElement = driver.find_element_by_id("input")
inputElement.send_keys(LNKINPUT)
inputElement.send_keys(Keys.ENTER)
#time.sleep(2)

wait = WebDriverWait(driver, 120)
wait.until(EC.visibility_of_element_located((By.ID, 'buttons')))
est = driver.find_element_by_link_text("Download")
est.click()

def every_downloads_chrome(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")
    return driver.execute_script("""
        return document.querySelector('downloads-manager')
        .shadowRoot.querySelector('#downloadsList')
        .items.filter(e => e.state === 'COMPLETE')
        .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url);
        """)
        
paths = WebDriverWait(driver, 120, 1).until(every_downloads_chrome)
print(paths)
time.sleep(2)
driver.quit()
