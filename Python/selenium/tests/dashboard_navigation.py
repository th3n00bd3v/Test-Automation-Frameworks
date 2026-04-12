import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# Import helper functions
from utils.data_helper import BASE_URL, get_latest_user

def dashboard_navigation():
   
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    
    try:
        # Retrieves recently registered user after registration test has run
        user = get_latest_user()
        print(f"[INFO] Login attempted - Username: {user['username']}")

        driver.get(BASE_URL)
        
        wait = WebDriverWait(driver, 10)
        
        # Navigate to login page
        login_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_page.click()
        
        # Attempt login with the retrieved user credentials
        username = wait.until(EC.presence_of_element_located((By.ID, "UserName")))
        username.send_keys(user["username"])
        
        password = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password.send_keys(user["password"])
        

        # Clicking the 'Log in' submit button
        time.sleep(1)
        signin_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class,'btn-signin')]")))
        signin_button.click()
        
        # Give the page a moment to load the authenticated state
        
        time.sleep(1)
        
        if wait.until(EC.presence_of_element_located((By.XPATH, "//form[@action='/Account/Logout']"))):
            print(f"[PASS] Successfully logged in as {user['username']}")
        else:
            print("[FAIL] Login failed. 'Log off' link not detected.")

        # Access employees dashboard
        
        employees = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'Employee')]")))
        employees.click()
        
        time.sleep(2)
        
        # Scroll to bottom of the page to ensure list is loaded
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    dashboard_navigation() 
        
        