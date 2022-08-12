from select import select
from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

web="https://www.cinepolis.com.sv/"
path="/home/ngochez/Documentos/Proyecto/msedgedriver"

driver= webdriver.Edge(path)
driver.get(web)

ciudad= Select(driver.find_element(By.ID,'cmbCiudades'))
ciudad.select_by_visible_text('Santa Ana, El Salvador')

sala= Select(driver.find_element(By.ID,'cmbComplejos'))
sala.select_by_visible_text('Cinépolis Metrocentro Santa Ana')
