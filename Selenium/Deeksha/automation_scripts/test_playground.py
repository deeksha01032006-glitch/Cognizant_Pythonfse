"""
test_playground.py
Updated sample pytest suite for Hands-on 6.
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    driver.get(base_url + "simple-form-demo/")
    wait = WebDriverWait(driver, 10)

    inputs = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
    )

    target = next((e for e in inputs if e.is_displayed() and e.is_enabled()), None)
    assert target is not None

    target.clear()
    target.send_keys(message)
    assert target.get_attribute("value") == message


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo/")
    wait = WebDriverWait(driver, 10)

    checkbox = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo/")
    wait = WebDriverWait(driver, 10)

    dropdown = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "select"))
    )

    select = Select(dropdown)

    select.select_by_visible_text("Wednesday")

    # Re-locate the dropdown because the page refreshes the DOM
    dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "select"))
    )

    select = Select(dropdown)

    selected = driver.execute_script("""
    return arguments[0].options[
    arguments[0].selectedIndex
    ].text;
    """, dropdown)

    assert selected == "Wednesday"