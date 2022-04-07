# selenium-async

Make Selenium easy to by managing a browser pool, and `asyncio` compatibility!

-   Source: [https://github.com/munro/python-selenium-async](https://github.com/munro/python-selenium-async)
-   Documentation: [https://selenium-async.readthedocs.io/en/latest/](https://selenium-async.readthedocs.io/en/latest/)

## install

```bash
poetry add selenium-async
```

## usage

```python
import selenium_async


def get_title(driver: selenium_async.WebDriver):
    driver.get("https://www.python.org/")
    return driver.title

print(await selenium_async.run_sync(get_title))

# prints: Welcome to Python.org
```

## license

MIT
