from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_selenium_firefox():
    # Setup Firefox driver using WebDriver Manager
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    
    ## Set full screen size
    driver.maximize_window()

## Registration test for EAApp


    # Open a website
    baseurl = "http://eaapp.somee.com/"
    driver.get(baseurl)
    print(driver.title)
    time.sleep(2)    
        
    # Click on the Register link
    register_link = driver.find_element(By.LINK_TEXT, "Register")
    register_link.click()
    print(driver.title)
    
    time.sleep(2)
    # Fill in the registration form
    username = driver.find_element(By.ID, "UserName")
    username.send_keys("iyer8798")
    
    time.sleep(2)
    email = driver.find_element(By.ID, "Email")
    email.send_keys("iyer8798@example.com")
    
    time.sleep(2)
    password = driver.find_element(By.ID, "Password")
    password.send_keys("Pas$w0rd@123")
    
    time.sleep(2)
    confirm_password = driver.find_element(By.ID, "ConfirmPassword")
    confirm_password.send_keys("Pas$w0rd@123")
    
    time.sleep(2)
    register_button = driver.find_element(By.XPATH, "//button[@class='btn-register']")
    register_button.click()

if __name__ == "__main__":
    test_selenium_firefox()