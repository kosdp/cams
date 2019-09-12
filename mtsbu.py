from selenium import webdriver
import time

try:
	driver = webdriver.Chrome()
	driver.get('http://policy-web.mtsbu.ua')
	driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/ul/li[1]').click()
	time.sleep(1)
	driver.find_element_by_name('RegNoModel.PlateNumber').send_keys('AE8462CX')
	driver.find_element_by_name('RegNoModel.Date').clear().send_keys('01.01.2019')
	driver.find_element_by_id('submitBtn').click()

finally:
	#driver.quit()
	pass
