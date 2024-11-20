#Automated script thatGoes to Titan22.com and logs in with the username and password #provided and visits the contact us page


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('no-sandbox')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument("start-maximized")
  options.add_argument("disable-infobars")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable- automation"])

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")

  return driver


def main():
  driver = get_driver()
  
  #Logging in:
  driver.find_element(
      by="id", value="CustomerEmail").send_keys("ahmedsarpak999@gmail.com")
  driver.find_element(by="id", value="CustomerPassword").send_keys("Ahmed@267")
 
  driver.find_element(
      by="xpath",
      value="/html/body/main/article/section/div/div[1]/form/button").click()
  time.sleep(2)
  
  #Clicking on Contact us page
  driver.find_element(
      by="xpath",
      value=
      "/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a"
  ).click()
  time.sleep(2)
  print(driver.current_url)


print(main())
