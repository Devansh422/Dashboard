from timeit import default_timer
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
#from webdriver_manager.firefox import GeckoDriverManager  # Note "GeckoDriverManager"
def fox():
    start=default_timer()
    options=Options()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Firefox(options=options)#,service=Service(GeckoDriverManager().install()))
    driver.get("http://127.0.0.1:5500/scarp-1.html")
    elem=driver.find_element(By.ID,'username')
    elem2=driver.find_element(By.ID,'password')
    elem3=driver.find_element(By.ID,'loginbutton')
    #elem.clear()
    #elem2.clear()
    elem.send_keys("2023B0101021")
    elem2.send_keys("Rob09953")
    elem3.click()
    end=default_timer()
    driver.quit()
    print("Success")
    print(f"Elapsed time: {end-start}")

