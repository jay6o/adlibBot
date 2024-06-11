from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def filters(driver):
  filter_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[4]/div[2]/div[1]/div/div[3]/div/div/div/div/div/div/div/span/div/div/div[2]")))
  filter_select.click()
  media_type_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div")))
  media_type_select.click()
  video_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div")))
  video_radio.click()
  active_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div[5]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div")))
  active_select.click()
  active_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div")))
  active_radio.click()
  apply_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[3]/div/div[2]/div/span/div/div/div")))
  apply_button.click()






