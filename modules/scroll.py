import time

def scroll(driver, stop_scrolling):
  scroll_height = 1
  while not stop_scrolling:
    for i in range(500):
      driver.execute_script(f"window.scrollBy(0, {scroll_height});")

    time.sleep(1)
