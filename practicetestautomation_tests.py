# practicetestautomation_tests.py
# Site: https://practicetestautomation.com/practice-test-login/
# Practice Test Automation login and navigation test cases.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://practicetestautomation.com/practice-test-login/"
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"

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
    """Case 1: Valid login with student/Password123."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "submit").click()
        wait.until(EC.url_contains("/logged-in-successfully/"))
        success = driver.find_element(By.CLASS_NAME, "post-title")
        assert "Logged In Successfully" in success.text
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
        driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys("wrongpassword")
        driver.find_element(By.ID, "submit").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
        assert "Your password is invalid" in error.text
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
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "submit").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
        assert "Your username is invalid" in error.text
        print("CASE 3 (invalid login - wrong username): PASS")
    except Exception as error:
        print("CASE 3 (invalid login - wrong username): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login_fields():
    """Case 4: Login with empty username and password."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "submit").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
        assert "username is required" in error.text.lower() or "password is required" in error.text.lower()
        print("CASE 4 (empty login fields): PASS")
    except Exception as error:
        print("CASE 4 (empty login fields): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_students_page():
    """Case 5: Navigate to Students page."""
    driver, wait = start()
    try:
        driver.get("https://practicetestautomation.com/")
        students_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Students")))
        students_link.click()
        wait.until(EC.url_contains("/practice-test-students/"))
        heading = driver.find_element(By.CLASS_NAME, "entry-title").text
        assert "Students" in heading
        print("CASE 5 (students page): PASS")
    except Exception as error:
        print("CASE 5 (students page): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_teachers_page():
    """Case 6: Navigate to Teachers page."""
    driver, wait = start()
    try:
        driver.get("https://practicetestautomation.com/")
        teachers_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Teachers")))
        teachers_link.click()
        wait.until(EC.url_contains("/practice-test-teachers/"))
        heading = driver.find_element(By.CLASS_NAME, "entry-title").text
        assert "Teachers" in heading
        print("CASE 6 (teachers page): PASS")
    except Exception as error:
        print("CASE 6 (teachers page): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_courses_page():
    """Case 7: Navigate to Courses page."""
    driver, wait = start()
    try:
        driver.get("https://practicetestautomation.com/")
        courses_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Courses")))
        courses_link.click()
        wait.until(EC.url_contains("/practice-test-courses/"))
        heading = driver.find_element(By.CLASS_NAME, "entry-title").text
        assert "Courses" in heading
        print("CASE 7 (courses page): PASS")
    except Exception as error:
        print("CASE 7 (courses page): FAIL -", error)
    finally:
        stop(driver)

def test_navigate_to_grades_page():
    """Case 8: Navigate to Grades page."""
    driver, wait = start()
    try:
        driver.get("https://practicetestautomation.com/")
        grades_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Grades")))
        grades_link.click()
        wait.until(EC.url_contains("/practice-test-grades/"))
        heading = driver.find_element(By.CLASS_NAME, "entry-title").text
        assert "Grades" in heading
        print("CASE 8 (grades page): PASS")
    except Exception as error:
        print("CASE 8 (grades page): FAIL -", error)
    finally:
        stop(driver)

def test_logout_after_login():
    """Case 9: Login then logout."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "submit").click()
        wait.until(EC.url_contains("/logged-in-successfully/"))
        logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()
        wait.until(EC.url_contains("/practice-test-login/"))
        print("CASE 9 (logout): PASS")
    except Exception as error:
        print("CASE 9 (logout): FAIL -", error)
    finally:
        stop(driver)

def test_check_error_message_visibility():
    """Case 10: Verify error message appears and can be dismissed."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "submit").click()
        error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
        assert error.is_displayed()
        print("CASE 10 (error message visibility): PASS")
    except Exception as error:
        print("CASE 10 (error message visibility): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login_wrong_password()
    test_invalid_login_wrong_username()
    test_empty_login_fields()
    test_navigate_to_students_page()
    test_navigate_to_teachers_page()
    test_navigate_to_courses_page()
    test_navigate_to_grades_page()
    test_logout_after_login()
    test_check_error_message_visibility()
