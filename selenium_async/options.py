from dataclasses import KW_ONLY, dataclass
from typing import Literal

BrowserType = Literal["firefox", "chrome"]


@dataclass(frozen=True, eq=True, order=True)
class Options:
    _: KW_ONLY
    browser: BrowserType = "firefox"
    headless: bool = True
