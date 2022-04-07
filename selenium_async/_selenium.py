import atexit
import warnings
import weakref

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxBase
from selenium.webdriver.remote.webdriver import WebDriver as WebDriverBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# don't tell me what to do!
warnings.filterwarnings(
    "ignore",
    message="find_element_by_css_selector is deprecated. Please use find_element(by=By.CSS_SELECTOR, value=css_selector) instead",
)


class WebDriver(WebDriverBase):
    running: bool

    def get_blank(self):
        raise NotImplementedError


class WebdriverMixin(WebDriver, object):
    running: bool

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def _atexit():
            self.quit()

        def _finalizer(_driver: WebDriver):
            # @TODO this isn't working, ugh!
            _driver.quit()

        self.running = True
        self.__atexit__ = atexit.register(_atexit)
        self._finalizer = weakref.finalize(self, _finalizer, self)

    def close(self):
        try:
            super().close()
        except:
            pass

    def quit(self):
        try:
            atexit.unregister(self.__atexit__)
        except:
            pass
        try:
            self.close()
        except:
            pass
        try:
            super().close()
        except:
            pass
        self.running = False


class Firefox(WebdriverMixin, WebDriver, FirefoxBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_blank(self):
        self.get("about:blank")


(TimeoutException, By, Keys, FirefoxOptions, FirefoxBase, EC, WebDriverWait,) = (
    TimeoutException,
    By,
    Keys,
    FirefoxOptions,
    FirefoxBase,
    EC,
    WebDriverWait,
)
