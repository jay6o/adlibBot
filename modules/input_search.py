import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def input_search(driver, search_terms):
  ad_type_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]")))
  ad_type_select.click()
  all_ads = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div[1]/input")))
  all_ads.click()
  search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/input")))
  search_input.click()
  search_input.send_keys(search_terms, Keys.RETURN)
  return


