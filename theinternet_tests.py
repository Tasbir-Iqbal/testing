# theinternet_tests.py
# Site: https://the-internet.herokuapp.com/
# The Internet HerokuApp comprehensive test cases for all sections.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

BASE_URL = "https://the-internet.herokuapp.com/"

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
    """Case 1: Valid login with tomsmith/SecretPassword!"""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        wait.until(EC.url_contains("/secure"))
        success = driver.find_element(By.ID, "flash")
        assert "You logged into a secure area!" in success.text
        print("CASE 1 (valid login): PASS")
    except Exception as error:
        print("CASE 1 (valid login): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login():
    """Case 2: Invalid login with wrong credentials."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "login")
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "Your username is invalid!" in error.text
        print("CASE 2 (invalid login): PASS")
    except Exception as error:
        print("CASE 2 (invalid login): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login():
    """Case 3: Login with empty fields."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "login")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
        assert "username is required" in error.text.lower() or "password is required" in error.text.lower()
        print("CASE 3 (empty login): PASS")
    except Exception as error:
        print("CASE 3 (empty login): FAIL -", error)
    finally:
        stop(driver)

def test_checkboxes():
    """Case 4: Check and uncheck checkboxes."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "checkboxes")
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        # Uncheck first, check second
        if checkboxes[0].is_selected():
            checkboxes[0].click()
        if not checkboxes[1].is_selected():
            checkboxes[1].click()
        assert not checkboxes[0].is_selected()
        assert checkboxes[1].is_selected()
        print("CASE 4 (checkboxes): PASS")
    except Exception as error:
        print("CASE 4 (checkboxes): FAIL -", error)
    finally:
        stop(driver)

def test_dropdown():
    """Case 5: Select from dropdown."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "dropdown")
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 1")
        assert dropdown.first_selected_option.text == "Option 1"
        dropdown.select_by_visible_text("Option 2")
        assert dropdown.first_selected_option.text == "Option 2"
        print("CASE 5 (dropdown): PASS")
    except Exception as error:
        print("CASE 5 (dropdown): FAIL -", error)
    finally:
        stop(driver)

def test_hover():
    """Case 6: Hover over element."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "hovers")
        figure = driver.find_element(By.CSS_SELECTOR, "div.figure")
        ActionChains(driver).move_to_element(figure).perform()
        time.sleep(1)
        caption = driver.find_element(By.CSS_SELECTOR, "div.figure h5")
        assert "name: user1" in caption.text.lower()
        print("CASE 6 (hover): PASS")
    except Exception as error:
        print("CASE 6 (hover): FAIL -", error)
    finally:
        stop(driver)

def test_file_upload():
    """Case 7: Upload a file."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "upload")
        # Create a temp file for upload
        temp_file = "/tmp/test_upload.txt"
        with open(temp_file, "w") as f:
            f.write("Test file content")
        file_input = driver.find_element(By.ID, "file-upload")
        file_input.send_keys(temp_file)
        driver.find_element(By.ID, "file-submit").click()
        success = wait.until(EC.visibility_of_element_located((By.ID, "uploaded-files")))
        assert "test_upload.txt" in success.text
        print("CASE 7 (file upload): PASS")
    except Exception as error:
        print("CASE 7 (file upload): FAIL -", error)
    finally:
        stop(driver)

def test_dynamic_content():
    """Case 8: Check dynamic content loading."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "dynamic_content")
        initial_content = driver.find_element(By.ID, "content").text
        driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        time.sleep(2)
        new_content = driver.find_element(By.ID, "content").text
        assert initial_content != new_content
        print("CASE 8 (dynamic content): PASS")
    except Exception as error:
        print("CASE 8 (dynamic content): FAIL -", error)
    finally:
        stop(driver)

def test_dynamic_controls():
    """Case 9: Add and remove elements."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "dynamic_controls")
        # Remove element
        remove_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")
        remove_btn.click()
        wait.until(EC.invisibility_of_element_located((By.ID, "checkbox")))
        # Add element
        add_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")
        add_btn.click()
        wait.until(EC.visibility_of_element_located((By.ID, "checkbox")))
        print("CASE 9 (dynamic controls): PASS")
    except Exception as error:
        print("CASE 9 (dynamic controls): FAIL -", error)
    finally:
        stop(driver)

def test_inputs():
    """Case 10: Enter number in input field."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "inputs")
        input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
        input_field.clear()
        input_field.send_keys("123")
        assert input_field.get_attribute("value") == "123"
        print("CASE 10 (inputs): PASS")
    except Exception as error:
        print("CASE 10 (inputs): FAIL -", error)
    finally:
        stop(driver)

def test_multiple_windows():
    """Case 11: Open new window and switch."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "windows")
        original_window = driver.current_window_handle
        driver.find_element(By.LINK_TEXT, "Click Here").click()
        wait.until(lambda d: len(d.window_handles) > 1)
        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break
        assert "New Window" in driver.title
        driver.close()
        driver.switch_to.window(original_window)
        print("CASE 11 (multiple windows): PASS")
    except Exception as error:
        print("CASE 11 (multiple windows): FAIL -", error)
    finally:
        stop(driver)

def test_notification_messages():
    """Case 12: Trigger and check notification."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "notification_messages_rendered")
        driver.find_element(By.LINK_TEXT, "click here").click()
        notification = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "example")))
        assert "Notification Message" in notification.text
        print("CASE 12 (notification messages): PASS")
    except Exception as error:
        print("CASE 12 (notification messages): FAIL -", error)
    finally:
        stop(driver)

def test_redirect():
    """Case 13: Check redirect link."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "redirector")
        driver.find_element(By.LINK_TEXT, "here").click()
        wait.until(EC.url_contains("/status/200"))
        assert "/status/200" in driver.current_url
        print("CASE 13 (redirect): PASS")
    except Exception as error:
        print("CASE 13 (redirect): FAIL -", error)
    finally:
        stop(driver)

def test_status_codes():
    """Case 14: Check status code page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "status_codes")
        driver.find_element(By.LINK_TEXT, "200").click()
        wait.until(EC.url_contains("/200"))
        assert "200" in driver.current_url
        print("CASE 14 (status codes): PASS")
    except Exception as error:
        print("CASE 14 (status codes): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_empty_login()
    test_checkboxes()
    test_dropdown()
    test_hover()
    test_file_upload()
    test_dynamic_content()
    test_dynamic_controls()
    test_inputs()
    test_multiple_windows()
    test_notification_messages()
    test_redirect()
    test_status_codes()
