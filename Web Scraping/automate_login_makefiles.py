# Automates login process and then scrapes the temperature displayed on the website 
# every two seconds and stores it in a new file with the current date and time as 
# filename


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('no-sandbox')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable- automation"])

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/login/")

  return driver

def clean_text(text):
  output = float(text.split(": ")[1])
  return output


def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  print(driver.current_url)
  time.sleep(2)

  x = 1
  while x < 3:  
   value = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
   temp = str(clean_text(value.text))
   ct = datetime.datetime.now().strftime('%Y-%m-%d.%H:%M:%S')
   print(f"The current temperature is {temp} at {ct}")
   with open(f"{ct}.txt", "a") as file:
    file.write(f"{temp}")
    file.close() 
   time.sleep(2)
   x = x + 1 
  

print(main())
