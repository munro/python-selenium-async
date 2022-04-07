import asyncio
from timeit import default_timer

import pytest

import selenium_async


@pytest.mark.integration
async def test_pool():
    cool_urls = [
        "http://python.com",
        "https://news.ycombinator.com/",
        "https://www.reddit.com/",
        "https://www.yahoo.com/",
        "https://www.google.com/",
        "https://www.forbes.com/",
        "https://twitter.com/",
    ]

    def cool(driver: selenium_async.WebDriver):

        import random

        start = default_timer()

        url = random.choice(cool_urls)

        driver.get(url)
        finish = default_timer()
        driver.get_blank()

        duration = finish - start
        return start, duration, url, driver.title

    async def _main():
        driver = selenium_async.launch_sync(selenium_async.Options(headless=False))
        driver.get("http://python.org")

        begin = default_timer()

        results = await asyncio.gather(
            *(selenium_async.run_sync(cool, headless=False) for _ in range(10))
        )

        for i, (start, duration, url, title) in enumerate(results):
            time_offset = start - begin
            print(
                f"[INDEX {i}] [OFFSET {time_offset:6.3f}] [DURATION {duration:6.3f}] {url} -- {title}"
            )

    await _main()
