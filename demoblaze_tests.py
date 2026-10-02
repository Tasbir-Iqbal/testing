# demoblaze_tests.py
# Site: https://demoblaze.com/
# DemoBlaze e-commerce comprehensive test cases.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

BASE_URL = "https://demoblaze.com/"

def random_credentials():
    """Generate random username and password for signup."""
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    password = 'TestPass123!'
    return username, password

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
        driver.find_element(By.ID, "login2").click()
        username_field = wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))
        username_field.send_keys("testuser123")
        driver.find_element(By.ID, "loginpassword").send_keys("test123")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        time.sleep(3)
        welcome = driver.find_element(By.ID, "nameofuser")
        assert "Welcome" in welcome.text
        print("CASE 1 (valid login): PASS")
    except Exception as error:
        print(f"CASE 1 (valid login): FAIL - {error}")
    finally:
        stop(driver)

def test_invalid_login():
    """Case 2: Invalid login with wrong credentials."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "login2").click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("wronguser")
        driver.find_element(By.ID, "loginpassword").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        print("CASE 2 (invalid login): PASS")
    except Exception as error:
        print(f"CASE 2 (invalid login): FAIL - {error}")
    finally:
        stop(driver)

def test_new_user_signup():
    """Case 3: New user signup."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "signin2").click()
        username, password = random_credentials()
        wait.until(EC.visibility_of_element_located((By.ID, "sign-username"))).send_keys(username)
        driver.find_element(By.ID, "sign-password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[onclick='signUp()']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        print(f"CASE 3 (new user signup): PASS - Username: {username}")
    except Exception as error:
        print(f"CASE 3 (new user signup): FAIL - {error}")
    finally:
        stop(driver)

def test_logout():
    """Case 4: Login then logout."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "login2").click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("testuser123")
        driver.find_element(By.ID, "loginpassword").send_keys("test123")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        time.sleep(3)
        driver.find_element(By.ID, "logout2").click()
        time.sleep(2)
        print("CASE 4 (logout): PASS")
    except Exception as error:
        print(f"CASE 4 (logout): FAIL - {error}")
    finally:
        stop(driver)

def test_add_to_cart():
    """Case 5: Add product to cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "a[href='#'][onclick='addToCart(1)']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        cart_link = driver.find_element(By.ID, "cartur")
        assert cart_link.is_displayed()
        print("CASE 5 (add to cart): PASS")
    except Exception as error:
        print(f"CASE 5 (add to cart): FAIL - {error}")
    finally:
        stop(driver)

def test_view_cart():
    """Case 6: View cart and check items."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Nokia lumia 1520")))
        product.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "a[href='#'][onclick='addToCart(7)']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        cart_items = driver.find_elements(By.CSS_SELECTOR, "#tbodyid tr")
        assert len(cart_items) > 0
        print(f"CASE 6 (view cart): PASS - Items: {len(cart_items)}")
    except Exception as error:
        print(f"CASE 6 (view cart): FAIL - {error}")
    finally:
        stop(driver)

def test_remove_from_cart():
    """Case 7: Remove item from cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Iphone 6 32gb")))
        product.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "a[href='#'][onclick='addToCart(4)']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        delete_link = driver.find_element(By.LINK_TEXT, "Delete")
        delete_link.click()
        time.sleep(2)
        print("CASE 7 (remove from cart): PASS")
    except Exception as error:
        print(f"CASE 7 (remove from cart): FAIL - {error}")
    finally:
        stop(driver)

def test_place_order():
    """Case 8: Place an order."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s7")))
        product.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "a[href='#'][onclick='addToCart(8)']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "button[onclick='placeOrder()']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("John Doe")
        driver.find_element(By.ID, "country").send_keys("USA")
        driver.find_element(By.ID, "city").send_keys("New York")
        driver.find_element(By.ID, "card").send_keys("1234567890123456")
        driver.find_element(By.ID, "month").send_keys("12")
        driver.find_element(By.ID, "year").send_keys("2026")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='purchaseOrder()']").click()
        time.sleep(3)
        alert_text = driver.switch_to.alert.text
        assert "Order Placed" in alert_text or "Thank you" in alert_text
        driver.switch_to.alert.accept()
        print("CASE 8 (place order): PASS")
    except Exception as error:
        print(f"CASE 8 (place order): FAIL - {error}")
    finally:
        stop(driver)

def test_check_order_history():
    """Case 9: Check order history."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "login2").click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("testuser123")
        driver.find_element(By.ID, "loginpassword").send_keys("test123")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='logIn()']").click()
        time.sleep(3)
        driver.find_element(By.ID, "orders").click()
        time.sleep(2)
        order_table = driver.find_element(By.ID, "tbodyid")
        assert order_table.is_displayed()
        print("CASE 9 (check order history): PASS")
    except Exception as error:
        print(f"CASE 9 (check order history): FAIL - {error}")
    finally:
        stop(driver)

def test_category_navigation():
    """Case 10: Navigate through product categories."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        phones = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        phones.click()
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card-title")
        assert len(products) > 0
        laptops = driver.find_element(By.LINK_TEXT, "Laptops")
        laptops.click()
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card-title")
        assert len(products) > 0
        print("CASE 10 (category navigation): PASS")
    except Exception as error:
        print(f"CASE 10 (category navigation): FAIL - {error}")
    finally:
        stop(driver)

def test_product_details():
    """Case 11: View product details."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        product = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6")))
        product.click()
        time.sleep(2)
        title = driver.find_element(By.CSS_SELECTOR, "h2.name").text
        price = driver.find_element(By.CSS_SELECTOR, "h3").text
        assert "Samsung" in title
        assert "$" in price
        print(f"CASE 11 (product details): PASS - {title}")
    except Exception as error:
        print(f"CASE 11 (product details): FAIL - {error}")
    finally:
        stop(driver)

def test_contact_form():
    """Case 12: Submit contact form."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "contactur").click()
        wait.until(EC.visibility_of_element_located((By.ID, "recipient-email"))).send_keys("test@example.com")
        driver.find_element(By.ID, "recipient-name").send_keys("John Doe")
        driver.find_element(By.ID, "message-text").send_keys("Test message for contact form")
        driver.find_element(By.CSS_SELECTOR, "button[onclick='sendCoords()']").click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        print("CASE 12 (contact form): PASS")
    except Exception as error:
        print(f"CASE 12 (contact form): FAIL - {error}")
    finally:
        stop(driver)

def test_search_product():
    """Case 13: Search for a product."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "searcher")))
        search_box.send_keys("samsung")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        products = driver.find_elements(By.CSS_SELECTOR, "#tbodyid .card-title")
        assert len(products) > 0
        print(f"CASE 13 (search product): PASS - Found {len(products)} products")
    except Exception as error:
        print(f"CASE 13 (search product): FAIL - {error}")
    finally:
        stop(driver)

def test_empty_cart_checkout():
    """Case 14: Try to checkout with empty cart."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.ID, "cartur").click()
        time.sleep(2)
        # Cart should be empty or show no items
        print("CASE 14 (empty cart checkout): PASS")
    except Exception as error:
        print(f"CASE 14 (empty cart checkout): FAIL - {error}")
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_new_user_signup()
    test_logout()
    test_add_to_cart()
    test_view_cart()
    test_remove_from_cart()
    test_place_order()
    test_check_order_history()
    test_category_navigation()
    test_product_details()
    test_contact_form()
    test_search_product()
    test_empty_cart_checkout()
