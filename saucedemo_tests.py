# saucedemo_tests.py
# Site: https://www.saucedemo.com/
# SauceDemo (Swag Labs) login and shopping cart test cases.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

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
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys(VALID_USERNAME)
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(VALID_PASSWORD)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        wait.until(EC.url_contains("/inventory.html"))
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" in title
        print("CASE 1 (valid login): PASS")
    except Exception as error:
        print("CASE 1 (valid login): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login_locked_out():
    """Case 2: Login with locked out user."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("locked_out_user")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(VALID_PASSWORD)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
        assert "locked out" in error.text.lower()
        print("CASE 2 (locked out user): PASS")
    except Exception as error:
        print("CASE 2 (locked out user): FAIL -", error)
    finally:
        stop(driver)

def test_invalid_login_wrong_credentials():
    """Case 3: Login with wrong username and password."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.send_keys("wronguser")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("wrongpass")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
        assert "Username and password do not match" in error.text
        print("CASE 3 (wrong credentials): PASS")
    except Exception as error:
        print("CASE 3 (wrong credentials): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login_fields():
    """Case 4: Try to login with empty fields."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        error = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
        assert "Username is required" in error.text
        print("CASE 4 (empty login fields): PASS")
    except Exception as error:
        print("CASE 4 (empty login fields): FAIL -", error)
    finally:
        stop(driver)

def test_add_to_cart():
    """Case 5: Login and add product to cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_button.click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"
        print("CASE 5 (add to cart): PASS")
    except Exception as error:
        print("CASE 5 (add to cart): FAIL -", error)
    finally:
        stop(driver)

def test_remove_from_cart():
    """Case 6: Add to cart then remove."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badges) == 0
        print("CASE 6 (remove from cart): PASS")
    except Exception as error:
        print("CASE 6 (remove from cart): FAIL -", error)
    finally:
        stop(driver)

def test_sort_products():
    """Case 7: Sort products by price."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        dropdown.click()
        dropdown.find_element(By.XPATH, "//option[@value='priceasc']").click()
        time.sleep(1)
        print("CASE 7 (sort products): PASS")
    except Exception as error:
        print("CASE 7 (sort products): FAIL -", error)
    finally:
        stop(driver)

def test_view_cart():
    """Case 8: Add to cart and view cart page."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()
        wait.until(EC.url_contains("/cart.html"))
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert "Shopping Cart" in title
        print("CASE 8 (view cart): PASS")
    except Exception as error:
        print("CASE 8 (view cart): FAIL -", error)
    finally:
        stop(driver)

def test_checkout():
    """Case 9: Complete checkout process."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()
        wait.until(EC.url_contains("/checkout-step-one.html"))
        driver.find_element(By.ID, "first-name").send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        wait.until(EC.url_contains("/checkout-step-two.html"))
        driver.find_element(By.ID, "finish").click()
        wait.until(EC.url_contains("/checkout-complete.html"))
        heading = driver.find_element(By.TAG_NAME, "h2").text
        assert "Thank you" in heading
        print("CASE 9 (checkout): PASS")
    except Exception as error:
        print("CASE 9 (checkout): FAIL -", error)
    finally:
        stop(driver)

def test_logout():
    """Case 10: Login then logout."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "user-name").send_keys(VALID_USERNAME)
        driver.find_element(By.ID, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        wait.until(EC.url_contains("/inventory.html"))
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        menu.click()
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        wait.until(EC.url_contains("/index.html"))
        print("CASE 10 (logout): PASS")
    except Exception as error:
        print("CASE 10 (logout): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login_locked_out()
    test_invalid_login_wrong_credentials()
    test_empty_login_fields()
    test_add_to_cart()
    test_remove_from_cart()
    test_sort_products()
    test_view_cart()
    test_checkout()
    test_logout()
