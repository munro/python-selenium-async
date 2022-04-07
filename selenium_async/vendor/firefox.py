from selenium_async._selenium import Firefox


def firefox_get_browser_pid(driver: Firefox) -> int:
    if driver.service is not None and driver.service.process is not None:
        print(driver.service.process.pid)
        print(driver.service.__dict__)
        print(driver.service.process.__dict__)
    raise NotImplementedError("@TODO get pid so we can kill it if geckodriver dies")
