import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# Import helper functions
from utils.data_helper import BASE_URL, get_latest_user

def login_registered_user():
   
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

        manage_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/Manage']")))
        manage_page.click()
        
        # Verify user details visible
                
        assert wait.until(EC.presence_of_element_located((By.XPATH, f"//dd[contains(text(),'{user['username']}')]"))), "[FAIL] Username not matching."         
        print(f"[PASS] Username '{user['username']}' is validated.")
        assert wait.until(EC.presence_of_element_located((By.XPATH, f"//dd[contains(text(),'{user['email']}')]"))), "[FAIL] Email not matching."
        print(f"[PASS] Email '{user['email']}' is validated.")
        time.sleep(1)
        
    finally:
        # Close the browser to clean up the test environment
        time.sleep(2)
        driver.quit()
        
if __name__ == "__main__":
    login_registered_user()