from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

lnkin = input("Enter/Paste your Youtube URL:")

#Chrome Options
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#Launch Chrome
browser = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
download_dir = tempfile.TemporaryDirectory().name
os.mkdir(download_dir)

#Download without asking
browser.command_executor._commands["send_command"] = (
    "POST',
    '/session/$sessionId/chromium/send_command'
)
params = {
    'cmd': 'Page.setDownloadBehavior',
    'params': {
        'behavior': 'allow',
        'downloadPath': download_dir
    }
}

browser.execute("send_command", params)

#Execute YTmp3

browser.get("https://ytmp3.cc/en13/")

IE = browser.find_element_by_id("input")
IE.send_keys(lnkin)
IE.send_keys(Keys.ENTER)

wait = WebDriverWait(browser, 120)
wait.until(EC.visibility_of_element_located((By.ID, 'buttons')))
est = browser.find_element_by_link_text("Download")
est.click()

browser.quit()