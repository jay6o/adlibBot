from selenium import webdriver
from modules.input_search import input_search
from modules.filters import filters
from modules.scroll import scroll
import threading
from pynput import keyboard

def start():  
  search_terms = input("Enter your search terms: ")
  driver = webdriver.Chrome()
  driver.get("https://www.facebook.com/ads/library/")
  t1 = threading.Thread()
  input_search(driver, search_terms)
  filters(driver)
  global stop_scrolling
  stop_scrolling = False
  scroll(driver, stop_scrolling)
  driver.quit()


if __name__ == "__main__":
  start()

