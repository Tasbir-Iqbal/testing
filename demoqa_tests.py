# demoqa_tests.py
# Site: https://demoqa.com/
# DemoQA comprehensive test cases for forms, alerts, windows, and more.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

BASE_URL = "https://demoqa.com/"

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

def test_registration_form_success():
    """Case 1: Fill and submit registration form successfully."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-test-registration/")
        driver.find_element(By.ID, "firstName").send_keys("John")
        driver.find_element(By.ID, "lastName").send_keys("Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
        driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()
        driver.find_element(By.ID, "userNumber").send_keys("1234567890")
        driver.find_element(By.ID, "dateOfBirthInput").click()
        driver.find_element(By.CSS_SELECTOR, ".react-datepicker__current-month").click()
        Select(driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-dropdown")).select_by_visible_text("January")
        Select(driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-dropdown")).select_by_visible_text("2000")
        driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--001").click()
        driver.find_element(By.ID, "currentAddress").send_keys("123 Test Street")
        Select(driver.find_element(By.ID, "state")).select_by_visible_text("NCR")
        Select(driver.find_element(By.ID, "city")).select_by_visible_text("Delhi")
        driver.find_element(By.ID, "submit").click()
        wait.until(EC.visibility_of_element_located((By.ID, "example-modal-schemas-title")))
        print("CASE 1 (registration form): PASS")
    except Exception as error:
        print("CASE 1 (registration form): FAIL -", error)
    finally:
        stop(driver)

def test_simple_alert():
    """Case 2: Trigger and accept simple alert."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-alerts/")
        driver.find_element(By.ID, "alertButton").click()
        alert = wait.until(EC.alert_is_present())
        assert "You clicked a button" in alert.text
        alert.accept()
        print("CASE 2 (simple alert): PASS")
    except Exception as error:
        print("CASE 2 (simple alert): FAIL -", error)
    finally:
        stop(driver)

def test_confirm_alert():
    """Case 3: Trigger and accept confirm alert."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-alerts/")
        driver.find_element(By.ID, "confirmButton").click()
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        result = driver.find_element(By.ID, "confirmResult")
        assert "You selected Ok" in result.text
        print("CASE 3 (confirm alert): PASS")
    except Exception as error:
        print("CASE 3 (confirm alert): FAIL -", error)
    finally:
        stop(driver)

def test_prompt_alert():
    """Case 4: Trigger prompt alert and enter text."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-alerts/")
        driver.find_element(By.ID, "promtButton").click()
        alert = wait.until(EC.alert_is_present())
        alert.send_keys("Test Input")
        alert.accept()
        result = driver.find_element(By.ID, "promptResult")
        assert "Test Input" in result.text
        print("CASE 4 (prompt alert): PASS")
    except Exception as error:
        print("CASE 4 (prompt alert): FAIL -", error)
    finally:
        stop(driver)

def test_new_browser_window():
    """Case 5: Click button to open new browser window."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-browser-tabs/")
        original_window = driver.current_window_handle
        driver.find_element(By.ID, "tabButton").click()
        wait.until(lambda d: len(d.window_handles) > 1)
        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break
        assert "DemoQA" in driver.title
        driver.close()
        driver.switch_to.window(original_window)
        print("CASE 5 (new browser window): PASS")
    except Exception as error:
        print("CASE 5 (new browser window): FAIL -", error)
    finally:
        stop(driver)

def test_new_browser_tab():
    """Case 6: Click button to open new browser tab."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-browser-tabs/")
        original_window = driver.current_window_handle
        driver.find_element(By.ID, "browserWindow").click()
        wait.until(lambda d: len(d.window_handles) > 1)
        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break
        assert "DemoQA" in driver.title
        driver.close()
        driver.switch_to.window(original_window)
        print("CASE 6 (new browser tab): PASS")
    except Exception as error:
        print("CASE 6 (new browser tab): FAIL -", error)
    finally:
        stop(driver)

def test_upload_file():
    """Case 7: Upload a file."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-upload-download/")
        temp_file = "/tmp/test_upload.txt"
        with open(temp_file, "w") as f:
            f.write("Test upload content")
        file_input = driver.find_element(By.ID, "uploadFile")
        file_input.send_keys(temp_file)
        driver.find_element(By.ID, "uploadButton").click()
        wait.until(EC.visibility_of_element_located((By.ID, "uploadedFilePath")))
        uploaded = driver.find_element(By.ID, "uploadedFilePath").text
        assert "test_upload.txt" in uploaded
        print("CASE 7 (upload file): PASS")
    except Exception as error:
        print("CASE 7 (upload file): FAIL -", error)
    finally:
        stop(driver)

def test_download_file():
    """Case 8: Download a file."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-upload-download/")
        driver.find_element(By.ID, "downloadButton").click()
        time.sleep(3)
        print("CASE 8 (download file): PASS")
    except Exception as error:
        print("CASE 8 (download file): FAIL -", error)
    finally:
        stop(driver)

def test_visible_textboxes():
    """Case 9: Enter text in visible textboxes."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-text-box/")
        driver.find_element(By.ID, "userName").send_keys("John Doe")
        driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
        driver.find_element(By.ID, "permanentAddress").send_keys("456 Permanent Ave")
        driver.find_element(By.ID, "submit").click()
        print("CASE 9 (visible textboxes): PASS")
    except Exception as error:
        print("CASE 9 (visible textboxes): FAIL -", error)
    finally:
        stop(driver)

def test_hidden_textboxes():
    """Case 10: Find and interact with hidden textboxes."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-text-box/")
        hidden_field = driver.find_element(By.ID, "hiddenField")
        assert not hidden_field.is_displayed()
        print("CASE 10 (hidden textboxes): PASS")
    except Exception as error:
        print("CASE 10 (hidden textboxes): FAIL -", error)
    finally:
        stop(driver)

def test_radio_buttons():
    """Case 11: Select radio buttons."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-radio-buttons/")
        radio_impressive = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
        radio_impressive.click()
        assert radio_impressive.find_element(By.CSS_SELECTOR, "input[type='radio']").is_selected()
        print("CASE 11 (radio buttons): PASS")
    except Exception as error:
        print("CASE 11 (radio buttons): FAIL -", error)
    finally:
        stop(driver)

def test_checkboxes():
    """Case 12: Check and uncheck checkboxes."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "/practice-checkbox/")
        checkbox1 = driver.find_element(By.CSS_SELECTOR, "label[for='checkbox1']")
        checkbox1.click()
        assert checkbox1.find_element(By.CSS_SELECTOR, "input[type='checkbox']").is_selected()
        print("CASE 12 (checkboxes): PASS")
    except Exception as error:
        print("CASE 12 (checkboxes): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_registration_form_success()
    test_simple_alert()
    test_confirm_alert()
    test_prompt_alert()
    test_new_browser_window()
    test_new_browser_tab()
    test_upload_file()
    test_download_file()
    test_visible_textboxes()
    test_hidden_textboxes()
    test_radio_buttons()
    test_checkboxes()
