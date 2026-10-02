# Test Automation Repository

A comprehensive collection of automated test scripts for various practice websites, designed for exam preparation and learning Selenium WebDriver and API testing.

## 📋 Overview

This repository contains **10 test files** with **114+ test cases** covering:
- Login/Authentication flows
- E-commerce operations (cart, checkout, orders)
- Banking transactions
- Form submissions
- UI widget interactions
- REST API CRUD operations
- File upload/download
- Alerts, dialogs, and popups
- Dynamic content handling
- Multiple windows/tabs

## 🗂️ Test Files

### 1. OrangeHRM Tests (`orangehrm_tests.py`)
**Site:** https://opensource-demo.orangehrmlive.com/

**Test Cases (7):**
- Valid login
- Invalid login (wrong password)
- Invalid login (wrong username)
- Navigate to Admin page
- Navigate to PIM page
- Navigate to Leave page
- Empty login fields

**Run:**
```bash
python orangehrm_tests.py
```

---

### 2. SauceDemo Tests (`saucedemo_tests.py`)
**Site:** https://www.saucedemo.com/

**Test Cases (10):**
- Valid login
- Invalid login (locked out user)
- Invalid login (wrong credentials)
- Empty login fields
- Add to cart
- Remove from cart
- Sort products
- View cart
- Complete checkout
- Logout

**Run:**
```bash
python saucedemo_tests.py
```

---

### 3. The Internet Tests (`theinternet_tests.py`)
**Site:** https://the-internet.herokuapp.com/

**Test Cases (14):**
- Valid login
- Invalid login
- Empty login
- Checkboxes
- Dropdown selection
- Hover actions
- File upload
- Dynamic content
- Dynamic controls
- Input fields
- Multiple windows
- Notification messages
- Redirect links
- Status codes

**Run:**
```bash
python theinternet_tests.py
```

---

### 4. Practice Test Automation Tests (`practicetestautomation_tests.py`)
**Site:** https://practicetestautomation.com/

**Test Cases (10):**
- Valid login
- Invalid login (wrong password)
- Invalid login (wrong username)
- Empty login fields
- Navigate to Students page
- Navigate to Teachers page
- Navigate to Courses page
- Navigate to Grades page
- Logout after login
- Error message visibility

**Run:**
```bash
python practicetestautomation_tests.py
```

---

### 5. DemoQA Tests (`demoqa_tests.py`)
**Site:** https://demoqa.com/

**Test Cases (12):**
- Registration form submission
- Simple alert
- Confirm alert
- Prompt alert
- New browser window
- New browser tab
- File upload
- File download
- Visible textboxes
- Hidden textboxes
- Radio buttons
- Checkboxes

**Run:**
```bash
python demoqa_tests.py
```

---

### 6. Automation Exercise Tests (`automationexercise_tests.py`)
**Site:** https://automationexercise.com/

**Test Cases (12):**
- Valid login
- Invalid login
- New user signup
- Existing email signup
- Search product
- Add to cart
- Remove from cart
- Contact form submission
- Products page navigation
- Test Cases page navigation
- Logout
- Empty login fields

**Run:**
```bash
python automationexercise_tests.py
```

---

### 7. Parabank Tests (`parabank_tests.py`)
**Site:** https://parabank.parasoft.com/

**Test Cases (10):**
- Valid login
- Invalid login
- Empty login
- Open new account
- Check account list
- Transfer money
- Pay bill
- Check transactions
- Logout
- Find transactions

**Run:**
```bash
python parabank_tests.py
```

---

### 8. Restful Booker Tests (`restfulbooker_tests.py`)
**Site:** https://restful-booker.herokuapp.com/

**Test Cases (10) - API Testing:**
- Create booking (POST)
- Get booking by ID (GET)
- Get nonexistent booking (404)
- Update booking with PUT
- Update booking with PATCH
- Delete booking (DELETE)
- Auth token success
- Auth token invalid (403)
- Update without auth (403)
- Health check (ping)

**Requirements:**
```bash
pip install requests
```

**Run:**
```bash
python restfulbooker_tests.py
```

---

### 9. DemoBlaze Tests (`demoblaze_tests.py`)
**Site:** https://demoblaze.com/

**Test Cases (14):**
- Valid login
- Invalid login
- New user signup
- Logout
- Add to cart
- View cart
- Remove from cart
- Place order
- Check order history
- Category navigation
- Product details
- Contact form
- Search product
- Empty cart checkout

**Run:**
```bash
python demoblaze_tests.py
```

---

### 10. jQuery UI Tests (`jqueryui_tests.py`)
**Site:** https://jqueryui.com/

**Test Cases (15):**
- Datepicker
- Slider
- Progress bar
- Tabs
- Dialog (open/close)
- Autocomplete
- Menu
- Tooltip
- Button
- Checkbox/Radio
- Select menu
- Spinner
- Accordion
- Resizable
- Droppable (drag & drop)

**Run:**
```bash
python jqueryui_tests.py
```

---

## 🛠️ Prerequisites

### Required Software
- **Python 3.7+** installed
- **Chrome browser** installed
- **ChromeDriver** matching your Chrome version

### Python Dependencies

Install required packages:
```bash
pip install selenium requests
```

### ChromeDriver Setup

1. Check your Chrome version: `chrome://version/`
2. Download matching ChromeDriver: https://chromedriver.chromium.org/downloads
3. Add ChromeDriver to your system PATH, or place it in the same folder as the test files

---

## 🚀 Quick Start

### Run All Tests
```bash
# Run individual test files
python orangehrm_tests.py
python saucedemo_tests.py
python theinternet_tests.py
# ... and so on for each file
```

### Run Specific Test Case
Edit the `if __name__ == "__main__":` section in any file to call specific test functions.

---

## 📁 Project Structure

```
testing/
├── README.md
├── orangehrm_tests.py
├── saucedemo_tests.py
├── theinternet_tests.py
├── practicetestautomation_tests.py
├── demoqa_tests.py
├── automationexercise_tests.py
├── parabank_tests.py
├── restfulbooker_tests.py
├── demoblaze_tests.py
└── jqueryui_tests.py
```

---

## 🎯 Test Coverage Summary

| Category | Files | Total Cases |
|----------|-------|-------------|
| Login/Authentication | 10 files | 30+ cases |
| E-commerce/Cart | 4 files | 25+ cases |
| Forms & Input | 6 files | 20+ cases |
| Navigation | 5 files | 15+ cases |
| UI Widgets | 2 files | 20+ cases |
| API Testing | 1 file | 10 cases |
| File Operations | 2 files | 4 cases |
| Alerts/Dialogs | 3 files | 8+ cases |
| **TOTAL** | **10 files** | **114+ cases** |

---

## 💡 Tips for Exam Success

1. **Understand the pattern:** Most test cases follow this structure:
   - Start browser
   - Navigate to URL
   - Find element(s)
   - Interact (click, send_keys, etc.)
   - Assert/verify
   - Close browser

2. **Common locators to know:**
   - `By.ID`
   - `By.NAME`
   - `By.CSS_SELECTOR`
   - `By.XPATH`
   - `By.LINK_TEXT`
   - `By.CLASS_NAME`

3. **Important waits:**
   - `WebDriverWait` with `expected_conditions`
   - `visibility_of_element_located`
   - `element_to_be_clickable`
   - `url_contains`

4. **Common assertions:**
   - Check page title
   - Verify URL contains text
   - Verify element text
   - Check element is displayed

5. **For API tests:**
   - Understand HTTP methods (GET, POST, PUT, PATCH, DELETE)
   - Know status codes (200, 201, 400, 403, 404)
   - Use `requests` library
   - Handle JSON responses

---

## 🔧 Troubleshooting

### ChromeDriver Issues
```
Message: 'chromedriver' executable needs to be in PATH
```
**Solution:** Download ChromeDriver and add to PATH or specify path:
```python
from selenium.webdriver.chrome.service import Service
service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)
```

### Element Not Found
```
selenium.common.exceptions.NoSuchElementException
```
**Solution:** 
- Check if element is in iframe (switch to frame first)
- Add explicit waits
- Verify locator is correct

### Element Not Interactable
```
selenium.common.exceptions.ElementNotInteractableException
```
**Solution:**
- Wait for element visibility
- Scroll to element
- Check for overlays

---

## 📚 Learning Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Python Requests](https://docs.python-requests.org/)
- [Expected Conditions](https://selenium-python.readthedocs.io/api.html#expected-conditions)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

---

## 📝 Notes

- All tests use **Chrome browser** in maximized mode
- Each test function is **independent** and can run alone
- Browsers close automatically after each test (with 2-second delay)
- Test output shows **PASS/FAIL** for each case
- **Do not close browser manually** while tests are running

---

## 🎓 Exam Preparation Checklist

- [ ] Can write a valid login test
- [ ] Can write an invalid login test
- [ ] Can add items to cart
- [ ] Can fill and submit forms
- [ ] Can handle alerts/popups
- [ ] Can work with dropdowns
- [ ] Can upload files
- [ ] Can switch between windows/tabs
- [ ] Can use XPATH and CSS selectors
- [ ] Can write API tests (GET/POST/PUT/DELETE)
- [ ] Can add assertions/verifications
- [ ] Can use explicit waits

---

## 📄 License

This repository is for educational and practice purposes.

---

**Happy Testing! 🚀**
