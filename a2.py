from selenium import webdriver
from time import sleep
import time

driver = webdriver.Chrome()
driver.get('https://www.bigbasket.com')
sleep(1)

t = time.localtime()
current_time = time.strftime("%H%M%S", t)

enter = input('next')
clickbar = driver.find_element_by_xpath('//*[@id="headerControllerId"]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/div/span/span[2]/span'.format(enter))
driver.execute_script("arguments[0].click();", clickbar)

name = input('Enter the location : ')
location = driver.find_element_by_xpath('//*[@id="headerControllerId"]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[1]/div/input[1]').send_keys(name)

clickbar1 = driver.find_element_by_xpath('//*[@id="ui-select-choices-row-1-0"]/a'.format(enter))
driver.execute_script("arguments[0].click();", clickbar1)


element = driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div/div/div/div/ul/li[2]/div/div/div[2]/form/div[3]/button')
driver.execute_script("arguments[0].click();", element)


keyword = input('Enter the keyword : ')
location = driver.find_element_by_xpath('//*[@id="input"]').send_keys(keyword)

elementX = driver.find_element_by_xpath('//*[@id="navbar-main"]/div/div[3]/div/div/button')
driver.execute_script("arguments[0].click();", elementX)


driver.get_screenshot_as_file(keyword+"_"+name+"_"+current_time+".png")
driver.quit()

print("end...")



