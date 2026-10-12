"""FastAPI / Starlette integration, see docs/install.rst."""

from collections.abc import Mapping
from pathlib import Path
from urllib.parse import urlencode

from starlette.staticfiles import StaticFiles

from pyoes.context import PyoesContext

STATIC_DIR = Path(__file__).parent / "static"

# PyoesContext field -> settings attribute (the pyramid ini key with "_" for ".")
SETTINGS = {
    "plausible_domain_hash": "plausible_domain_hash",
    "burgerprofiel_header_id": "burgerprofiel_header_id",
    "burgerprofiel_footer_id": "burgerprofiel_footer_id",
    "banner": "pyoes_banner",
    "banner_detail": "pyoes_banner_detail",
}


def mount_static(app, path="/pyoes_static", name="pyoes_static"):
    """Serve the pyoes static files, the counterpart of pyramid's ``pyoes_static`` view."""
    app.mount(path, StaticFiles(directory=STATIC_DIR), name=name)


def _setting(settings, key):
    if settings is None:
        return None
    if isinstance(settings, Mapping):
        return settings.get(key)
    return getattr(settings, key, None)


def context(
    request,
    *,
    settings=None,
    user=None,
    authenticated_userid=None,
    static_mount="static",
    pyoes_static_mount="pyoes_static",
    **overrides,
):
    """
    Build the ``pyoes`` template context for a starlette request.

    :param static_mount: name of the app's own static mount, used for asset
        specs like ``"myapp:static/css/app.css"``.
    :param overrides: explicit values for any :class:`PyoesContext` field.
    """

    def route_path(name, _query=None, **params):
        path = request.url_for(name, **params).path
        if _query:
            path = f"{path}?{urlencode(_query, doseq=True)}"
        return path

    def static_path(spec):
        package, _, asset = spec.rpartition(":")
        asset = asset.removeprefix("static/")
        mount = pyoes_static_mount if package == "pyoes" else static_mount
        return request.url_for(mount, path=asset).path

    values = {field: _setting(settings, key) for field, key in SETTINGS.items()}
    values.update(
        route_path=route_path,
        static_path=static_path,
        user=user,
        authenticated_userid=authenticated_userid,
    )
    values.update(overrides)
    return PyoesContext(**values)
