import asyncio
from dataclasses import KW_ONLY, dataclass, field
from functools import lru_cache
from typing import Dict

from selenium_async._selenium import WebDriver
from selenium_async.options import Options


@dataclass(init=False)
class Pool:
    _: KW_ONLY
    max_size: int
    blank_page_after_use: bool
    resources: Dict[Options, list[WebDriver]] = field(repr=False)
    semaphore: asyncio.Semaphore = field(repr=False)

    def __init__(
        self,
        *,
        max_size: int = 4,
        blank_page_after_use: bool = True,
    ) -> None:
        self.max_size = max_size
        self.blank_page_after_use = blank_page_after_use
        self.resources = {}
        self.semaphore = asyncio.Semaphore(max_size)

    def __len__(self):
        return sum(len(x) for x in self.resources.values())


@lru_cache()
def default_pool():
    return Pool()
