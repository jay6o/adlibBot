from selenium import webdriver
from modules.input_search import input_search
from modules.filters import filters
from modules.scroll import scroll

def start():  
  search_terms = input("Enter your search terms: ")
  driver = webdriver.Chrome()
  driver.get("https://www.facebook.com/ads/library/")
  input_search(driver, search_terms)
  filters(driver)
  stop_scrolling = False
  scroll(driver, stop_scrolling)
  driver.quit()


if __name__ == "__main__":
  start()

