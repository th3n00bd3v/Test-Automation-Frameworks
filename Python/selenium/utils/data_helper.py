import os
import json
import uuid
import random
import string

# Centralized URL for the entire project
BASE_URL = "http://eaapp.somee.com/"

def get_project_root():
    """Calculates the project root relative to this utility file."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

def get_data_file_path():
    """Returns the path to the registered_users.json in the 'test data' folder."""
    folder_path = os.path.join(get_project_root(), "test data")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return os.path.join(folder_path, "registered_users.json")

def generate_user_payload():
    """Creates randomized user data for registration."""
    uid = str(uuid.uuid4())[:8]
    chars = string.ascii_letters + string.digits + "!@#$"
    password = "".join(random.choice(chars) for _ in range(10)) + "1aA!"
    
    return {
        "username": f"AutoUser_{uid}",
        "email": f"tester_{uid}@example.com",
        "password": password
    }

def save_user(user_data):
    """Appends the newly registered user to our JSON file."""
    file_path = get_data_file_path()
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                pass
    data.append(user_data)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def get_latest_user():
    """Retrieves the most recently registered user for login tests."""
    file_path = get_data_file_path()
    if not os.path.exists(file_path):
        raise FileNotFoundError("Test data file empty...registration test run pending!")
    with open(file_path, "r") as f:
        users = json.load(f)
        return users[-1]