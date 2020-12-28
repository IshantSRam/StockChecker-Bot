# Module Import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
# Important Varibales
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

while True:
    # Amazon
    print("Amazon")
    # Ryzen 5 5600x
    driver.get("https://www.amazon.in/dp/B08166SLDF/?tag=espresso004b-20")
    stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text
    print(time.strftime("%H:%M:%S"),"AMD Ryzen 5 5600X",stock)
    if stock=="Currently unavailable.":
        print("Price - Unavailable")
    else:
        price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        print("Price -",price)
    time.sleep(2.5)

    # Ryzen 5 5800x
    driver.get("https://www.amazon.in/dp/B0815XFSGK?tag=espresso004b-20")
    stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text
    print(time.strftime("%H:%M:%S"),"AMD Ryzen 7 5800X",stock)
    if stock=="Currently unavailable.":
        print("Price - Unavailable")
    else:
        price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        print("Price -",price)
    time.sleep(2.5)

    # Ryzen 5 5900x
    driver.get("https://www.amazon.in/dp/B08164VTWH?tag=espresso004b-20")
    stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text
    print(time.strftime("%H:%M:%S"),"AMD Ryzen 9 5900X",stock)
    if stock=="Currently unavailable.":
        print("Price - Unavailable")
    else:
        price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        print("Price -",price)
    time.sleep(2.5)

    # Ryzen 5 5950x
    driver.get("https://www.amazon.in/dp/B0815Y8J9N?tag=espresso004b-20")
    stock = driver.find_element_by_xpath('//*[@id="availability"]/span').text
    print(time.strftime("%H:%M:%S"),"AMD Ryzen 9 5950X",stock)
    if stock=="Currently unavailable.":
        print("Price - Unavailable")
    else:
        price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        print("Price -",price)
    time.sleep(2.5)




