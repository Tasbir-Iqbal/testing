# orangehrm_tests.py
# Site: https://opensource-demo.orangehrmlive.com/
# OrangeHRM login and navigation test cases with detailed comments.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://opensource-demo.orangehrmlive.com/"
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"

def start():
    """Start Chrome browser with wait configuration."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    return driver, wait

def stop(driver):
    """Wait briefly then close browser."""
    time.sleep(2)
    driver.quit()

def test_valid_login():
    """Case 1: Valid login with correct credentials."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(VALID_USERNAME)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(VALID_PASSWORD)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        wait.until(EC.url_contains("/dashboard"))
        heading = driver.find_element(By.TAG_NAME, "h6").text
        assert "Dashboard" in heading
        print("CASE 1 (valid login): PASS")
    except Exception as error:
        print("CASE 1 (valid login): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login_wrong_password():
    """Case 2: Login with correct username but wrong password."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(VALID_USERNAME)
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("wrongpassword")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        error_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")))
        assert "Invalid credentials" in error_box.text
        print("CASE 2 (invalid login - wrong password): PASS")
    except Exception as error:
        print("CASE 2 (invalid login - wrong password): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login_wrong_username():
    """Case 3: Login with wrong username but correct password."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys("wronguser")
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(VALID_PASSWORD)
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        error_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-alert-content-text")))
        assert "Invalid credentials" in error_box.text
        print("CASE 3 (invalid login - wrong username): PASS")
    except Exception as error:
        print("CASE 3 (invalid login - wrong username): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_admin_page():
    """Case 4: After login, navigate to Admin page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(EC.url_contains("/dashboard"))
        admin_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
        admin_link.click()
        wait.until(EC.url_contains("/admin"))
        heading = driver.find_element(By.TAG_NAME, "h6").text
        assert "Admin" in heading
        print("CASE 4 (navigate to Admin): PASS")
    except Exception as error:
        print("CASE 4 (navigate to Admin): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_pim_page():
    """Case 5: After login, navigate to PIM page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(EC.url_contains("/dashboard"))
        pim_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_link.click()
        wait.until(EC.url_contains("/pim"))
        heading = driver.find_element(By.TAG_NAME, "h6").text
        assert "PIM" in heading
        print("CASE 5 (navigate to PIM): PASS")
    except Exception as error:
        print("CASE 5 (navigate to PIM): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_leave_page():
    """Case 6: After login, navigate to Leave page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(EC.url_contains("/dashboard"))
        leave_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']")))
        leave_link.click()
        wait.until(EC.url_contains("/leave"))
        heading = driver.find_element(By.TAG_NAME, "h6").text
        assert "Leave" in heading
        print("CASE 6 (navigate to Leave): PASS")
    except Exception as error:
        print("CASE 6 (navigate to Leave): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login_fields():
    """Case 7: Try to login with empty username and password."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        error_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message")))
        assert "Required" in error_box.text
        print("CASE 7 (empty login fields): PASS")
    except Exception as error:
        print("CASE 7 (empty login fields): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login_wrong_password()
    test_invalid_login_wrong_username()
    test_navigate_to_admin_page()
    test_navigate_to_pim_page()
    test_navigate_to_leave_page()
    test_empty_login_fields()
