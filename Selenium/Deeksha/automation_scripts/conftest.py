"""
===========================================================
Hands-On 6 : pytest Fixtures
Filename : conftest.py
===========================================================

This file contains:

1. Chrome Driver Fixture
2. Base URL Fixture
3. Screenshot on Failure Hook

"""

import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# =========================================================
# Driver Fixture
# =========================================================

@pytest.fixture(scope="function")
def driver(request):

    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    driver.implicitly_wait(10)

    # Make driver accessible inside hooks
    request.node.driver = driver

    yield driver

    driver.quit()


# =========================================================
# Base URL Fixture
# =========================================================

@pytest.fixture(scope="session")
def base_url():

    return "https://www.testmuai.com/selenium-playground/"


# =========================================================
# Screenshot on Failure
# =========================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            filename = os.path.join(
                "screenshots",
                f"{item.name}_failure.png"
            )

            try:
                driver.save_screenshot(filename)
                print(f"Screenshot saved : {filename}")
            except:
               pass

            print(f"\nScreenshot saved : {filename}")