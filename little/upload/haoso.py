from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver = webdriver.Chrome

ActionChains(driver).drag_and_drop(element1,element2).perform() #拖拽
driver.find_element_by_xpath(element).send_keys(Keys.ENTER) #Enter