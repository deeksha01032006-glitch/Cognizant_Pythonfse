"""
Hands-On 4
Selenium WebDriver Setup

Selenium Components

1. WebDriver
- WebDriver is the main Selenium component.
- It communicates directly with the browser using browser drivers.
- It performs browser actions like clicking buttons, entering text, and navigation.

2. Selenium Grid
- Selenium Grid allows tests to run on multiple browsers and multiple machines simultaneously.
- It is mainly used for parallel execution.

3. Selenium IDE
- Selenium IDE is a browser extension.
- It records and plays back browser actions.
- It can generate Selenium code automatically.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome Options
options = webdriver.ChromeOptions()

# Headless mode
options.add_argument("--headless")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Implicit Wait
driver.implicitly_wait(10)

# Implicit wait waits for every element globally.
# Explicit waits are preferred because they wait only when required,
# making scripts faster and more reliable.

# Open Website
driver.get("https://www.lambdatest.com/selenium-playground/")

# Print Title
print("Website Title:")
print(driver.title)

# -----------------------------
# Task 2
# -----------------------------

# Click Simple Form Demo
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

# Verify URL
assert "simple-form-demo" in driver.current_url

print("URL Verified")

# Navigate Back
driver.back()

time.sleep(2)

# Open Google in New Tab
driver.execute_script("window.open('https://www.google.com');")

# Print Window Handles
print("Window Handles:")
print(driver.window_handles)

# Switch to Google
driver.switch_to.window(driver.window_handles[1])

print("Google Title:")
print(driver.title)

# Switch Back
driver.switch_to.window(driver.window_handles[0])

# Screenshot
driver.save_screenshot("playground_screenshot.png")

print("Screenshot Saved")

# Window Size
print("Current Window Size:")
print(driver.get_window_size())

driver.set_window_size(1280, 800)

print("Updated Window Size:")
print(driver.get_window_size())

# Consistent window size ensures responsive UI behaves
# the same during every automation execution.

driver.quit()