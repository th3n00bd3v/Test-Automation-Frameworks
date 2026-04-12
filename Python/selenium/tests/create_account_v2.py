import sys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Path setup to import from utils

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))
from utils.data_helper import BASE_URL, generate_user_payload, save_user

def test_registration_navigation_flow():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    
    user = generate_user_payload()

    try:
        # Base URL from utils/data_helper.py
        driver.get(BASE_URL)
        
        wait = WebDriverWait(driver, 10)

        
        # Navigate to registration page
        register_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_page.click()
        
        # Registration form
        username = wait.until(EC.presence_of_element_located((By.ID, "UserName")))
        username.send_keys(user["username"])
        
        email = wait.until(EC.presence_of_element_located((By.ID, "Email")))
        email.send_keys(user["email"])
        
        password = wait.until(EC.presence_of_element_located((By.ID, "Password")))
        password.send_keys(user["password"])
        
        confirm_password = wait.until(EC.presence_of_element_located((By.ID, "ConfirmPassword")))
        confirm_password.send_keys(user["password"])

        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn-register')]")))
        register_button.click()
        
        save_user(user)
        print(f"User '{user['username']}' registered.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_registration_navigation_flow()