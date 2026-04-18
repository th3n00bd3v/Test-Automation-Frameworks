import sys
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

# Import helper functions
from utils.data_helper import (
    BASE_URL,
    get_latest_user,
    get_random_employee_id,
    save_employee_ids,
)

def fetch_employee_ids_from_page(wait):
    """Collect employee IDs from the Details links shown on the Employees page."""
    detail_links = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a.btn-detail[href*='/EmployeeDetails/Index/']")
        )
    )

    employee_ids = []
    for link in detail_links:
        href = link.get_attribute("href")
        match = re.search(r"/EmployeeDetails/Index/(\d+)", href)
        if match:
            employee_ids.append(match.group(1))

    return employee_ids

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
        
        ## Load employee ID from JSON or store first and load it 
        
        selected_employee_id = get_random_employee_id()
        
        
        if selected_employee_id:
            print(f"[INFO] Using cached employee ID from JSON: {selected_employee_id}")
            driver.get(f"{BASE_URL}EmployeeDetails/Index/{selected_employee_id}")
        else:
            print("[INFO] Employee ID cache not found. Fetching employee IDs from Employees page.")

            employees = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'Employee')]")))
            employees.click()
            time.sleep(2)

            employee_ids = fetch_employee_ids_from_page(wait)
            if not employee_ids:
                raise Exception("No employee detail links were found on the Employees page.")

            save_employee_ids(employee_ids)
            print(f"[INFO] Stored employee IDs in JSON: {employee_ids}")

            selected_employee_id = random.choice(employee_ids)
            
           # stored employee IDs in JSON: {employee_ids}")

            selected_employee_id = employee_ids[0]
            driver.get(f"{BASE_URL}EmployeeDetails/Index/{selected_employee_id}")

        wait.until(EC.url_contains(f"/EmployeeDetails/Index/{selected_employee_id}"))
        print(f"[PASS] Opened Employee Details page for employee ID: {selected_employee_id}")
        
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    dashboard_navigation() 
