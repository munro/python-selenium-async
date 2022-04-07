from selenium_async._selenium import (
    EC,
    By,
    Firefox,
    FirefoxBase,
    FirefoxOptions,
    Keys,
    TimeoutException,
    WebDriver,
    WebDriverWait,
)
from selenium_async.core import launch, launch_sync, run_sync, use_browser
from selenium_async.options import BrowserType, Options
from selenium_async.pool import Pool, default_pool

__version__ = "0.1.0"

run_sync, use_browser, launch, launch_sync = run_sync, use_browser, launch, launch_sync
BrowserType, Options = BrowserType, Options
Pool, default_pool = Pool, default_pool
(
    EC,
    By,
    Firefox,
    FirefoxBase,
    FirefoxOptions,
    Keys,
    TimeoutException,
    WebDriver,
    WebDriverWait,
) = (
    EC,
    By,
    Firefox,
    FirefoxBase,
    FirefoxOptions,
    Keys,
    TimeoutException,
    WebDriver,
    WebDriverWait,
)
