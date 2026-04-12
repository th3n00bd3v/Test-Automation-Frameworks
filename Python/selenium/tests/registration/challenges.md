## Challenge(s)

1. Register button was not getting detected due to default Firefox password manager popup showing while passing keys to Confirm password.
2. Register account button was not getting detected using `get element by link_text`. 
3. Username already exists shows if multiple iterations are run, since user is already created once. Is there a way to store these as environment variables once registration is done (i.e. convert this into a data-driven test)?

## Solution(s)

Upgraded the script with the help of Google Gemini by implementing the following fixes:

1. Configured FirefoxOptions to disable the browser's credential-saving prompts. This ensures a clean UI environment for the automation script.

    Implementation:
    ```
    options = Options()
    options.set_preference("signon.rememberSignons", False)
    options.set_preference("password_manager_enabled", False)
    ```
2. Switched to a more specific XPath targeting the input's value attribute. Additionally, implemented Explicit Waits (WebDriverWait) instead of static sleeps. This ensures the script waits for the element to be "clickable" in the DOM before attempting interaction, accounting for varying network speeds.

    ```
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Register']")))
    ```
3. Integrated a dynamic data generation strategy using the uuid library. By appending a unique identifier to the username and email, the test becomes idempotent (it can run infinitely without manual database resets).

    Example:
    ```
    import uuid
    unique_id = str(uuid.uuid4())[:8]
    username = f"user_{unique_id}"
### *Additional points*



1. *Install dependencies:*: Ensure webdriver-manager and selenium are updated.

2. *Import Options:* You must import from selenium.webdriver.firefox.options import Options.

3. *Replace time.sleep:* Transition to WebDriverWait to reduce "flakiness" and improve execution time.