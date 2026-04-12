from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_selenium_firefox():
    # Setup Firefox driver using WebDriver Manager
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    try:
        # Open a website
        driver.get("https://www.duckduckgo.com")

        # Validate title
        assert "DuckDuckGo" in driver.title

        print("Firefox opened on DuckDuckGo! Quitting now...")
        time.sleep(2)  # Sleep for 2 seconds to see the browser before quitting
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_selenium_firefox()