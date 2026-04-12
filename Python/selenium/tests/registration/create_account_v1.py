import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def registration_eaapp():
    # 1. Configure Firefox Options to disable password manager popups
    options = Options()
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("password_manager_enabled", False)

    # Setup Driver
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()

    # 2. Dynamic Data Generation (Ensures unique registration every time)
    unique_id = str(uuid.uuid4())[:8]
    user_data = {
        "username": f"user_{unique_id}",
        "email": f"test_{unique_id}@example.com",
        "password": "Pas$w0rd@123"
    }

    try:
        baseurl = "http://eaapp.somee.com/"
        driver.get(baseurl)
        
        # Using Explicit Waits instead of time.sleep
        wait = WebDriverWait(driver, 10)

        # Click Register
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill Form
        wait.until(EC.presence_of_element_located((By.ID, "UserName"))).send_keys(user_data["username"])
        driver.find_element(By.ID, "Email").send_keys(user_data["email"])
        driver.find_element(By.ID, "Password").send_keys(user_data["password"])
        driver.find_element(By.ID, "ConfirmPassword").send_keys(user_data["password"])

        # 3. Handling the Register Button
        # We use XPATH to find a button that contains the text 'Register'
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-register']")))
        register_button.click()

        print(f"Successfully registered user '{user_data['username']}' having email '{user_data['email']}'.")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        time.sleep(5) # See the result before quitting
        driver.quit()

if __name__ == "__main__":
    test_selenium_firefox()