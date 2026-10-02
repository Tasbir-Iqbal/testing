# jqueryui_tests.py
# Site: https://jqueryui.com/
# jQuery UI widget interaction test cases.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://jqueryui.com/"

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

def test_datepicker():
    """Case 1: Select a date from datepicker."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "datepicker/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        date_input = wait.until(EC.visibility_of_element_located((By.ID, "datepicker")))
        date_input.click()
        ui_datepicker = wait.until(EC.visibility_of_element_located((By.ID, "ui-datepicker-div")))
        assert ui_datepicker.is_displayed()
        # Select a day
        day = driver.find_element(By.CSS_SELECTOR, "td[data-day='15'] a")
        day.click()
        time.sleep(1)
        selected_value = date_input.get_attribute("value")
        assert selected_value != ""
        print(f"CASE 1 (datepicker): PASS - Selected: {selected_value}")
    except Exception as error:
        print(f"CASE 1 (datepicker): FAIL - {error}")
    finally:
        stop(driver)

def test_slider():
    """Case 2: Interact with slider."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "slider/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        slider = wait.until(EC.visibility_of_element_located((By.ID, "slider")))
        handle = slider.find_element(By.CSS_SELECTOR, ".ui-slider-handle")
        # Drag slider
        ActionChains(driver).drag_and_drop_by_offset(handle, 100, 0).perform()
        time.sleep(1)
        value = slider.get_attribute("aria-valuenow")
        assert value != "0"
        print(f"CASE 2 (slider): PASS - Value: {value}")
    except Exception as error:
        print(f"CASE 2 (slider): FAIL - {error}")
    finally:
        stop(driver)

def test_progress_bar():
    """Case 3: Check progress bar."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "progressbar/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        progress_bar = wait.until(EC.visibility_of_element_located((By.ID, "progressbar")))
        value = progress_bar.get_attribute("aria-valuenow")
        assert value is not None
        print(f"CASE 3 (progress bar): PASS - Value: {value}")
    except Exception as error:
        print(f"CASE 3 (progress bar): FAIL - {error}")
    finally:
        stop(driver)

def test_tabs():
    """Case 4: Switch between tabs."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "tabs/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        # Click second tab
        tab2 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proin elit arcu")))
        tab2.click()
        time.sleep(1)
        # Verify tab content changed
        tab_content = driver.find_element(By.ID, "tabs-2")
        assert tab_content.is_displayed()
        print("CASE 4 (tabs): PASS")
    except Exception as error:
        print(f"CASE 4 (tabs): FAIL - {error}")
    finally:
        stop(driver)

def test_dialog_open_close():
    """Case 5: Open and close dialog."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "dialog/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        # Open dialog
        open_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ui-button")))
        open_btn.click()
        time.sleep(1)
        # Verify dialog is open
        dialog = driver.find_element(By.ID, "dialog")
        assert dialog.is_displayed()
        # Close dialog
        close_btn = dialog.find_element(By.CSS_SELECTOR, "button.ui-button")
        close_btn.click()
        time.sleep(1)
        print("CASE 5 (dialog open/close): PASS")
    except Exception as error:
        print(f"CASE 5 (dialog open/close): FAIL - {error}")
    finally:
        stop(driver)

def test_autocomplete():
    """Case 6: Use autocomplete input."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "autocomplete/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        input_field = wait.until(EC.visibility_of_element_located((By.ID, "tags")))
        input_field.send_keys("ja")
        time.sleep(1)
        suggestions = driver.find_elements(By.CSS_SELECTOR, ".ui-autocomplete li")
        assert len(suggestions) > 0
        print(f"CASE 6 (autocomplete): PASS - Suggestions: {len(suggestions)}")
    except Exception as error:
        print(f"CASE 6 (autocomplete): FAIL - {error}")
    finally:
        stop(driver)

def test_menu():
    """Case 7: Interact with menu."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "menu/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        menu = wait.until(EC.visibility_of_element_located((By.ID, "menu")))
        # Hover over menu item
        menu_item = menu.find_element(By.LINK_TEXT, "Aberdeen")
        ActionChains(driver).move_to_element(menu_item).perform()
        time.sleep(1)
        submenu = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
        assert len(submenu) > 0
        print(f"CASE 7 (menu): PASS - Items: {len(submenu)}")
    except Exception as error:
        print(f"CASE 7 (menu): FAIL - {error}")
    finally:
        stop(driver)

def test_tooltip():
    """Case 8: Check tooltip."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "tooltip/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        # Hover over element with tooltip
        tooltip_element = wait.until(EC.visibility_of_element_located((By.ID, "tooltip")))
        ActionChains(driver).move_to_element(tooltip_element).perform()
        time.sleep(2)
        tooltip = driver.find_element(By.CSS_SELECTOR, ".ui-tooltip")
        assert tooltip.is_displayed()
        print("CASE 8 (tooltip): PASS")
    except Exception as error:
        print(f"CASE 8 (tooltip): FAIL - {error}")
    finally:
        stop(driver)

def test_button():
    """Case 9: Check styled buttons."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "button/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.ui-button")))
        assert len(buttons) > 0
        # Click a button
        buttons[0].click()
        time.sleep(1)
        print(f"CASE 9 (button): PASS - Buttons: {len(buttons)}")
    except Exception as error:
        print(f"CASE 9 (button): FAIL - {error}")
    finally:
        stop(driver)

def test_checkbox_radio():
    """Case 10: Check checkbox and radio widgets."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "checkboxradio/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        # Find and click a radio button
        radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='radio']")))
        radio.click()
        time.sleep(1)
        assert radio.is_selected()
        # Find and click a checkbox
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        checkbox.click()
        time.sleep(1)
        print("CASE 10 (checkbox/radio): PASS")
    except Exception as error:
        print(f"CASE 10 (checkbox/radio): FAIL - {error}")
    finally:
        stop(driver)

def test_selectmenu():
    """Case 11: Interact with select menu."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "selectmenu/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        select_btn = wait.until(EC.element_to_be_clickable((By.ID, "speed-button")))
        select_btn.click()
        time.sleep(1)
        options = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
        assert len(options) > 0
        # Select an option
        options[1].click()
        time.sleep(1)
        print(f"CASE 11 (selectmenu): PASS - Options: {len(options)}")
    except Exception as error:
        print(f"CASE 11 (selectmenu): FAIL - {error}")
    finally:
        stop(driver)

def test_spinner():
    """Case 12: Use number spinner."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "spinner/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        spinner = wait.until(EC.visibility_of_element_located((By.ID, "spinner")))
        initial_value = spinner.get_attribute("value")
        # Click up button
        up_btn = driver.find_element(By.CSS_SELECTOR, "a.ui-spinner-button.ui-spinner-up")
        up_btn.click()
        time.sleep(1)
        new_value = spinner.get_attribute("value")
        assert new_value != initial_value
        print(f"CASE 12 (spinner): PASS - {initial_value} -> {new_value}")
    except Exception as error:
        print(f"CASE 12 (spinner): FAIL - {error}")
    finally:
        stop(driver)

def test_accordion():
    """Case 13: Expand accordion sections."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "accordion/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        # Click second accordion header
        header2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3.ui-accordion-header:nth-of-type(2)")))
        header2.click()
        time.sleep(1)
        content2 = driver.find_element(By.CSS_SELECTOR, "div.ui-accordion-content:nth-of-type(2)")
        assert content2.is_displayed()
        print("CASE 13 (accordion): PASS")
    except Exception as error:
        print(f"CASE 13 (accordion): FAIL - {error}")
    finally:
        stop(driver)

def test_resizable():
    """Case 14: Resize element."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "resizable/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        resizable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.ui-resizable")))
        initial_width = resizable.size["width"]
        # Resize using handle
        handle = resizable.find_element(By.CSS_SELECTOR, ".ui-resizable-handle.ui-resizable-se")
        ActionChains(driver).drag_and_drop_by_offset(handle, 50, 50).perform()
        time.sleep(1)
        new_width = resizable.size["width"]
        assert new_width > initial_width
        print(f"CASE 14 (resizable): PASS - {initial_width}px -> {new_width}px")
    except Exception as error:
        print(f"CASE 14 (resizable): FAIL - {error}")
    finally:
        stop(driver)

def test_droppable():
    """Case 15: Drag and drop."""
    driver, wait = start()
    try:
        driver.get(BASE_URL + "droppable/")
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
        driver.switch_to.frame(iframe)
        draggable = wait.until(EC.visibility_of_element_located((By.ID, "draggable")))
        droppable = driver.find_element(By.ID, "droppable")
        # Drag and drop
        ActionChains(driver).drag_and_drop(draggable, droppable).perform()
        time.sleep(1)
        drop_text = droppable.text
        assert "Dropped" in drop_text or "ui-drop-hightlight" in droppable.get_attribute("class")
        print("CASE 15 (droppable): PASS")
    except Exception as error:
        print(f"CASE 15 (droppable): FAIL - {error}")
    finally:
        stop(driver)

if __name__ == "__main__":
    test_datepicker()
    test_slider()
    test_progress_bar()
    test_tabs()
    test_dialog_open_close()
    test_autocomplete()
    test_menu()
    test_tooltip()
    test_button()
    test_checkbox_radio()
    test_selectmenu()
    test_spinner()
    test_accordion()
    test_resizable()
    test_droppable()
