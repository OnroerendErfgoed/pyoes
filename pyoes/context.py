"""Framework-agnostic template context, available in the pyoes templates as ``pyoes``."""

from dataclasses import dataclass
from functools import lru_cache
from importlib.metadata import PackageNotFoundError
from importlib.metadata import packages_distributions
from importlib.metadata import version
from typing import Any
from typing import Callable


@lru_cache(maxsize=None)
def package_version(package):
    """
    Version of the installed distribution providing the python ``package``,
    or ``None``. Tries the package name itself first, then the distributions
    that install it (e.g. package ``beeldbankbeheer`` in distribution
    ``beeldbank``; this lookup does not work for editable installs).
    """
    if not package:
        return None
    for dist in (package, *packages_distributions().get(package, ())):
        try:
            return version(dist)
        except PackageNotFoundError:
            pass
    return None


VERSION = package_version("pyoes")


def asset_version(app_version=None, app_package=None):
    """
    Version appended to asset urls for cache busting: an explicit
    ``app_version``, else the version of ``app_package``, else the pyoes version.
    """
    return app_version or package_version(app_package) or VERSION


@dataclass(frozen=True)
class PyoesContext:
    """
    :param route_path: callable ``(name, **kw) -> str`` returning the path of
        a named route.
    :param static_path: callable turning an asset spec such as
        ``"myapp:static/css/app.css"`` into a url.
    :param app_version: version of the application, appended to asset urls
        for cache busting. Detected from ``app_package`` when not given.
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
    app_version: str | None = None

    def asset_version(self, app_package=None):
        return asset_version(self.app_version, app_package)

    @property
    def home_url(self):
        return self.route_path("home")
