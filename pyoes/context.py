"""Framework-agnostic template context, available in the pyoes templates as ``pyoes``."""

from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version
from typing import Any
from typing import Callable

try:
    VERSION = version("pyoes")
except PackageNotFoundError:  # pragma: no cover
    VERSION = None


@dataclass(frozen=True)
class PyoesContext:
    """
    :param route_path: callable ``(name, **kw) -> str`` returning the path of
        a named route.
    :param static_path: callable turning an asset spec such as
        ``"myapp:static/css/app.css"`` into a url.
    """

    route_path: Callable[..., str]
    static_path: Callable[[str], str]
    plausible_domain_hash: str | None = None
    burgerprofiel_header_id: str | None = None
    burgerprofiel_footer_id: str | None = None
    burgerprofiel_version: str | None = None
    banner: str | None = None
    banner_detail: str | None = None
    authenticated_userid: Any = None
    user: Any = None

    @property
    def version(self):
        """pyoes version, appended to asset urls in the layout for cache busting."""
        return VERSION

    @property
    def home_url(self):
        return self.route_path("home")
