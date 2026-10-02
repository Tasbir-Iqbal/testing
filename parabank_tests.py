# parabank_tests.py
# Site: https://parabank.parasoft.com/
# Parabank comprehensive test cases for banking operations.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

BASE_URL = "https://parabank.parasoft.com/"
VALID_USERNAME = "john"
VALID_PASSWORD = "demo"

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
    """Case 1: Valid login with john/demo."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        heading = driver.find_element(By.CSS_SELECTOR, "h1.title").text
        assert "Welcome" in heading
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
        driver.find_element(By.NAME, "username").send_keys("wronguser")
        driver.find_element(By.NAME, "password").send_keys("wrongpass")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "font[color='red']")))
        assert "login could not be completed" in error.text.lower()
        print("CASE 2 (invalid login): PASS")
    except Exception as error:
        print("CASE 2 (invalid login): FAIL -", error)
    finally:
        stop(driver)

def test_empty_login():
    """Case 3: Login with empty fields."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "font[color='red']")))
        assert "login could not be completed" in error.text.lower()
        print("CASE 3 (empty login): PASS")
    except Exception as error:
        print("CASE 3 (empty login): FAIL -", error)
    finally:
        stop(driver)

def test_open_account():
    """Case 4: Open a new savings account."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Open New Account").click()
        wait.until(EC.url_contains("/openaccount.do"))
        Select(driver.find_element(By.NAME, "newAccountType")).select_by_visible_text("SAVINGS")
        Select(driver.find_element(By.NAME, "fromAccountId")).select_by_index(1)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/openaccountconfirm.do"))
        success = driver.find_element(By.CSS_SELECTOR, "h1.title").text
        assert "Congratulations" in success
        print("CASE 4 (open account): PASS")
    except Exception as error:
        print("CASE 4 (open account): FAIL -", error)
    finally:
        stop(driver)

def test_check_account_list():
    """Case 5: Check account list after login."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        account_table = driver.find_element(By.ID, "accountTable")
        assert account_table.is_displayed()
        print("CASE 5 (check account list): PASS")
    except Exception as error:
        print("CASE 5 (check account list): FAIL -", error)
    finally:
        stop(driver)

def test_transfer_money():
    """Case 6: Transfer money between accounts."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        wait.until(EC.url_contains("/transfer.do"))
        driver.find_element(By.NAME, "amount").send_keys("10")
        Select(driver.find_element(By.NAME, "fromAccountId")).select_by_index(1)
        Select(driver.find_element(By.NAME, "toAccountId")).select_by_index(0)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/transferconfirm.do"))
        success = driver.find_element(By.CSS_SELECTOR, "h1.title").text
        assert "Transfer Complete!" in success
        print("CASE 6 (transfer money): PASS")
    except Exception as error:
        print("CASE 6 (transfer money): FAIL -", error)
    finally:
        stop(driver)

def test_pay_bill():
    """Case 7: Pay a bill."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Pay Bills").click()
        wait.until(EC.url_contains("/paybill.do"))
        driver.find_element(By.NAME, "payee").send_keys("Test Payee")
        driver.find_element(By.NAME, "address").send_keys("123 Bill Street")
        driver.find_element(By.NAME, "city").send_keys("Test City")
        driver.find_element(By.NAME, "state").send_keys("TS")
        driver.find_element(By.NAME, "zip").send_keys("12345")
        driver.find_element(By.NAME, "phoneNumber").send_keys("555-1234")
        driver.find_element(By.NAME, "accountNumber").send_keys("98765")
        driver.find_element(By.NAME, "confirmButton").click()
        wait.until(EC.url_contains("/paybillconfirm.do"))
        success = driver.find_element(By.CSS_SELECTOR, "h1.title").text
        assert "Bill Payment Complete" in success
        print("CASE 7 (pay bill): PASS")
    except Exception as error:
        print("CASE 7 (pay bill): FAIL -", error)
    finally:
        stop(driver)

def test_check_transactions():
    """Case 8: Check account transactions."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Account Activity").click()
        wait.until(EC.url_contains("/activity.do"))
        Select(driver.find_element(By.NAME, "accountId")).select_by_index(1)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "transactionTable")))
        table = driver.find_element(By.ID, "transactionTable")
        assert table.is_displayed()
        print("CASE 8 (check transactions): PASS")
    except Exception as error:
        print("CASE 8 (check transactions): FAIL -", error)
    finally:
        stop(driver)

def test_logout():
    """Case 9: Login then logout."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Logout").click()
        wait.until(EC.url_contains("/index.do"))
        print("CASE 9 (logout): PASS")
    except Exception as error:
        print("CASE 9 (logout): FAIL -", error)
    finally:
        stop(driver)

def test_find_transactions():
    """Case 10: Find transactions by date range."""
    driver, wait = start()
    try:
        driver.get(BASE_URL)
        driver.find_element(By.NAME, "username").send_keys(VALID_USERNAME)
        driver.find_element(By.NAME, "password").send_keys(VALID_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.url_contains("/overview.htm"))
        driver.find_element(By.LINK_TEXT, "Find Transactions").click()
        wait.until(EC.url_contains("/findTransactions.do"))
        driver.find_element(By.NAME, "minAmount").send_keys("0")
        driver.find_element(By.NAME, "maxAmount").send_keys("1000")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "transactionTable")))
        print("CASE 10 (find transactions): PASS")
    except Exception as error:
        print("CASE 10 (find transactions): FAIL -", error)
    finally:
        stop(driver)

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_empty_login()
    test_open_account()
    test_check_account_list()
    test_transfer_money()
    test_pay_bill()
    test_check_transactions()
    test_logout()
    test_find_transactions()
