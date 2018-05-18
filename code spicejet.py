from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=None
class SpiceJet:
	def chrome(self):	
		global driver
		driver=webdriver.Chrome(executable_path='D:\\newlib\\chromedriver.exe')
		driver.get('http://spicejet.com')
		driver.maximize_window()
		print('Browser Launched Successfully')
	
	def onewayroundtrip(self):
		global driver
		driver.find_element_by_id('ctl00_mainContent_rbtnl_Trip_0').click()
		driver.find_element_by_id('ctl00_mainContent_ddl_originStation1_CTXT').click()
		driver.find_element_by_link_text('Hyderabad (HYD)').click()
		time.sleep(3 )
		driver.find_element_by_link_text('Mumbai (BOM)').click()
		driver.find_element_by_link_text('17').click()
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Adult')).select_by_visible_text('3')
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Child')).select_by_visible_text('2')
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Infant')).select_by_visible_text('1')
		Select(driver.find_element_by_id('ctl00_mainContent_DropDownListCurrency')).select_by_visible_text('INR')
		driver.find_element_by_id('ctl00_mainContent_btn_FindFlights').click()
		time.sleep(5)
		driver.execute_script("window.history.go(-1)")
		driver.find_element_by_id('ctl00_mainContent_rbtnl_Trip_1').click()
		driver.find_element_by_id('ctl00_mainContent_ddl_originStation1_CTXT').click()
		driver.find_element_by_link_text('Delhi (DEL)').click()
		time.sleep(3 )
		driver.find_element_by_link_text('Pune (PNQ)').click()
		driver.find_element_by_link_text('20').click()
		time.sleep(3)
		driver.find_element_by_link_text('22').click()
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Adult')).select_by_visible_text('3')
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Child')).select_by_visible_text('2')
		Select(driver.find_element_by_id('ctl00_mainContent_ddl_Infant')).select_by_visible_text('1')
		Select(driver.find_element_by_id('ctl00_mainContent_DropDownListCurrency')).select_by_visible_text('INR')
		driver.find_element_by_id('ctl00_mainContent_btn_FindFlights').click()

sj=SpiceJet()
sj.chrome()
sj.onewayroundtrip()
