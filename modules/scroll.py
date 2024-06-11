import time

def scroll(driver, stop_scrolling):
  scroll_height = 750
  while not stop_scrolling:
    driver.execute_script(f"window.scrollBy(0, {scroll_height});")
    time.sleep(1) 
