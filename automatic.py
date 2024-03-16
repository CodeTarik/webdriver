from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_object = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service_object)
driver.get('https://de.wikipedia.org')
sleep(60)




try:
    driver.get('https://de.wikipedia.org')
except Exception as e:
    print(f"Fehler beim Öffnen der Webseite: {e}")

