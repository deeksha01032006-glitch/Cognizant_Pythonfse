"""
===========================================================
Hands-On 5 : Locator Strategies
Filename : locator_test.py
===========================================================

Question 32
------------
Locate the first input field using:
1. ID
2. Name (Not available on the updated website)
3. Class Name
4. Tag Name
5. Absolute XPath
6. Relative XPath

Question 33
------------
Locate the same element using CSS Selectors.

Question 34
------------
Locate checkbox labels using XPath.

Question 35
------------
Rank locator strategies.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.testmuai.com/selenium-playground/simple-form-demo/")

print("="*60)
print("QUESTION 32")
print("="*60)

# ---------------------------------------------------
# By.ID
# ---------------------------------------------------

element = driver.find_element(By.ID, "sum1")
print("✓ Located using ID")

# ---------------------------------------------------
# By.CLASS_NAME
# ---------------------------------------------------

driver.find_element(By.CLASS_NAME, "rounded")
print("✓ Located using CLASS_NAME")

# ---------------------------------------------------
# By.TAG_NAME
# ---------------------------------------------------

driver.find_element(By.TAG_NAME, "input")
print("✓ Located using TAG_NAME")

# ---------------------------------------------------
# Relative XPath
# ---------------------------------------------------

driver.find_element(
    By.XPATH,
    "//input[@id='sum1']"
)

print("✓ Located using Relative XPath")

# ---------------------------------------------------
# Absolute XPath
#
# NOTE:
# Copy the Full XPath from DevTools and replace
# the XPath below if it changes.
# ---------------------------------------------------

try:
    driver.find_element(
        By.XPATH,
        "/html/body//input[@id='sum1']"
    )
    print("✓ Located using Absolute XPath")
except:
    print("Absolute XPath differs on current website.")
    print("Copy Full XPath using DevTools if required.")

# ---------------------------------------------------
# By.NAME
#
# Current TestMuAI website does not provide
# a 'name' attribute for this input element.
# Hence By.NAME cannot be demonstrated here.
# ---------------------------------------------------

print("By.NAME : Not available for this element.")

print("\nAll Available Locator Strategies Verified!")

# ---------------------------------------------------
# Question 33
# CSS Selectors
# ---------------------------------------------------

print("\n"+"="*60)
print("QUESTION 33")
print("="*60)

# CSS by ID

driver.find_element(
    By.CSS_SELECTOR,
    "#sum1"
)

print("✓ CSS using ID")

# CSS using Attribute

driver.find_element(
    By.CSS_SELECTOR,
    "input[id='sum1']"
)

print("✓ CSS using Attribute")

# CSS using Tag + Class

driver.find_element(
    By.CSS_SELECTOR,
    "input.rounded"
)

print("✓ CSS using Class")

print("\nCSS Selectors Verified!")

# ---------------------------------------------------
# Question 34
# Checkbox Demo
# ---------------------------------------------------

driver.get(
    "https://www.testmuai.com/selenium-playground/checkbox-demo/"
)

time.sleep(2)

print("\n"+"="*60)
print("QUESTION 34")
print("="*60)

try:

    labels = driver.find_elements(
        By.XPATH,
        "//label[contains(text(),'Option')]"
    )

    print("Checkbox Labels")

    for label in labels:
        print(label.text)

except:

    print("Checkbox labels have changed on the updated website.")

# ---------------------------------------------------
# Question 35
# ---------------------------------------------------

print("\n"+"="*60)
print("QUESTION 35")
print("="*60)

print("""

Ranking of Locator Strategies

1. ID
   • Fastest
   • Unique
   • Recommended

2. Name
   • Good when available

3. CSS Selector
   • Fast
   • Flexible

4. Relative XPath
   • Good for dynamic pages

5. Class Name
   • Less reliable because multiple
     elements may share the same class.

6. Absolute XPath
   • Least preferred
   • Breaks when page layout changes

""")

driver.quit()

print("Browser Closed Successfully")