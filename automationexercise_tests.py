# automationexercise_tests.py
# Site: https://automationexercise.com/
# Automation Exercise comprehensive test cases for all features.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

BASE_URL = "https://automationexercise.com/"
VALID_USER_EMAIL = "test@example.com"
VALID_USER_PASSWORD = "password123"

def random_email():
    """Generate a random email for signup tests."""
    letters = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{letters}@newuser.com"

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
    """Case 1: Valid login with existing user."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))).send_keys(VALID_USER_EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(VALID_USER_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]")))
        print("CASE 1 (valid login): PASS")
    except Exception as error:
        print("CASE 1 (valid login): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login():
    """Case 2: Invalid login with wrong credentials."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))).send_keys("wrong@example.com")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-qa='login-error']")))
        assert "incorrect" in error.text.lower()
        print("CASE 2 (invalid login): PASS")
    except Exception as error:
        print("CASE 2 (invalid login): FAIL -", error)
    finally:
        stop(driver)

def test_new_user_signup():
    """Case 3: New user signup success."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        new_email = random_email()
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys("New User")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(new_email)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        driver.find_element(By.ID, "id_gender1").click()
        driver.find_element(By.ID, "password").send_keys("NewPass123")
        Select(driver.find_element(By.ID, "days")).select_by_value("10")
        Select(driver.find_element(By.ID, "months")).select_by_value("5")
        Select(driver.find_element(By.ID, "years")).select_by_value("1995")
        driver.find_element(By.ID, "first_name").send_keys("First")
        driver.find_element(By.ID, "last_name").send_keys("Last")
        driver.find_element(By.ID, "address1").send_keys("123 Street")
        Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
        driver.find_element(By.ID, "state").send_keys("State")
        driver.find_element(By.ID, "city").send_keys("City")
        driver.find_element(By.ID, "zipcode").send_keys("12345")
        driver.find_element(By.ID, "mobile_number").send_keys("0123456789")
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-button']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'ACCOUNT CREATED!')]")))
        print("CASE 3 (new user signup): PASS")
    except Exception as error:
        print("CASE 3 (new user signup): FAIL -", error)
    finally:
        stop(driver)

def test_existing_email_signup():
    """Case 4: Signup with existing email (should fail)."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys("Existing User")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(VALID_USER_EMAIL)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert-danger")))
        assert "exist" in error.text.lower()
        print("CASE 4 (existing email signup): PASS")
    except Exception as error:
        print("CASE 4 (existing email signup): FAIL -", error)
    finally:
        stop(driver)

def test_search_product():
    """Case 5: Search for a product."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='search-input']")))
        search_box.send_keys("tshirt")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        page_text = driver.find_element(By.TAG_NAME, "body").text
        assert "tshirt" in page_text.lower()
        print("CASE 5 (search product): PASS")
    except Exception as error:
        print("CASE 5 (search product): FAIL -", error)
    finally:
        stop(driver)

def test_add_to_cart():
    """Case 6: Add product to cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.productinfo button[data-product-id]"))).click()
        driver.find_element(By.XPATH, "//u[contains(text(), 'View Cart')]").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.cart_items")))
        cart_rows = driver.find_elements(By.CSS_SELECTOR, "table.cart_items tbody tr")
        assert len(cart_rows) > 0
        print("CASE 6 (add to cart): PASS")
    except Exception as error:
        print("CASE 6 (add to cart): FAIL -", error)
    finally:
        stop(driver)

def test_remove_from_cart():
    """Case 7: Remove product from cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.productinfo button[data-product-id]"))).click()
        driver.find_element(By.XPATH, "//u[contains(text(), 'View Cart')]").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.cart_items")))
        driver.find_element(By.CSS_SELECTOR, "a[data-item-removed]").click()
        time.sleep(1)
        cart_rows = driver.find_elements(By.CSS_SELECTOR, "table.cart_items tbody tr")
        assert len(cart_rows) == 0
        print("CASE 7 (remove from cart): PASS")
    except Exception as error:
        print("CASE 7 (remove from cart): FAIL -", error)
    finally:
        stop(driver)

def test_contact_form():
    """Case 8: Submit contact form."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Contact us')]").click()
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='name']").send_keys("Test User")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='email']").send_keys("test@example.com")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='subject']").send_keys("Test Subject")
        driver.find_element(By.CSS_SELECTOR, "textarea[data-qa='message']").send_keys("Test message")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='upload-file']").send_keys("/tmp/test.txt")
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='submit-button']").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.status.alert-success")))
        print("CASE 8 (contact form): PASS")
    except Exception as error:
        print("CASE 8 (contact form): FAIL -", error)
    finally:
        stop(driver)

def test_products_page():
    """Case 9: Navigate to products page and check heading."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Products')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'ALL PRODUCTS')]")))
        heading = driver.find_element(By.XPATH, "//h2[contains(text(), 'ALL PRODUCTS')]").text
        assert "ALL PRODUCTS" in heading
        print("CASE 9 (products page): PASS")
    except Exception as error:
        print("CASE 9 (products page): FAIL -", error)
    finally:
        stop(driver)

def test_test_cases_page():
    """Case 10: Navigate to test cases page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Test Cases')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'TEST CASES')]")))
        heading = driver.find_element(By.XPATH, "//h2[contains(text(), 'TEST CASES')]").text
        assert "TEST CASES" in heading
        print("CASE 10 (test cases page): PASS")
    except Exception as error:
        print("CASE 10 (test cases page): FAIL -", error)
    finally:
        stop(driver)

def test_logout():
    """Case 11: Login then logout."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-qa='login-email']"))).send_keys(VALID_USER_EMAIL)
        driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys(VALID_USER_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Logged in as')]")))
        driver.find_element(By.XPATH, "//a[contains(text(), 'Logout')]").click()
        wait.until(EC.url_contains("/index.php"))
        print("CASE 11 (logout): PASS")
    except Exception as error:
        print("CASE 11 (logout): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login_fields():
    """Case 12: Try to login with empty fields."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
        driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message")))
        assert "Required" in error.text
        print("CASE 12 (empty login fields): PASS")
    except Exception as error:
        print("CASE 12 (empty login fields): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_new_user_signup()
    test_existing_email_signup()
    test_search_product()
    test_add_to_cart()
    test_remove_from_cart()
    test_contact_form()
    test_products_page()
    test_test_cases_page()
    test_logout()
    test_empty_login_fields()
