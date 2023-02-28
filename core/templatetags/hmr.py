"""Custom tag inject HMR to vite-react
The code is mostly re-used from django-vite project (https://github.com/MrBin99/django-vite)

Basically creates a django tag that injects this script (that would be otherwise injected by Node)

  <script type="module">
  RefreshRuntime.injectIntoGlobalHook(window)
  window.$RefreshReg$ = () => {}
  window.$RefreshSig$ = () => (type) => type
  window.__vite_plugin_react_preamble_installed__ = true
  </script>

ref: https://vitejs.dev/guide/backend-integration.html
"""

from urllib.parse import urljoin

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


# If using in development or production mode.
DJANGO_VITE_REACT_HMR = getattr(settings, "DJANGO_VITE_REACT_HMR", "@react-refresh")

# If using in development or production mode.
DJANGO_VITE_DEV_MODE = getattr(settings, "DJANGO_VITE_DEV_MODE", False)

# Default Vite server protocol (http or https)
DJANGO_VITE_DEV_SERVER_PROTOCOL = getattr(
    settings, "DJANGO_VITE_DEV_SERVER_PROTOCOL", "http"
)

# Default vite server hostname.
DJANGO_VITE_DEV_SERVER_HOST = getattr(
    settings, "DJANGO_VITE_DEV_SERVER_HOST", "localhost"
)

# Default Vite server port.
DJANGO_VITE_DEV_SERVER_PORT = getattr(settings, "DJANGO_VITE_DEV_SERVER_PORT", 3000)

# Prefix for STATIC_URL
DJANGO_VITE_STATIC_URL_PREFIX = getattr(settings, "DJANGO_VITE_STATIC_URL_PREFIX", "")

DJANGO_VITE_STATIC_URL = urljoin(settings.STATIC_URL, DJANGO_VITE_STATIC_URL_PREFIX)

# Make sure 'DJANGO_VITE_STATIC_URL' finish with a '/'
if DJANGO_VITE_STATIC_URL[-1] != "/":
    DJANGO_VITE_STATIC_URL += "/"


def _generate_vite_server_url(path: str) -> str:
    """
    Generates an URL to and asset served by the Vite development server.

    Keyword Arguments:
        path {str} -- Path to the asset.

    Returns:
        str -- Full URL to the asset.
    """

    return urljoin(
        f"{DJANGO_VITE_DEV_SERVER_PROTOCOL}://"
        f"{DJANGO_VITE_DEV_SERVER_HOST}:{DJANGO_VITE_DEV_SERVER_PORT}",
        urljoin(DJANGO_VITE_STATIC_URL, path),
    )


def generate_vite_ws_client() -> str:
    """
    Generates the script tag for the Vite WS client for HMR.
    Only used in development, in production this method returns
    an empty string.

    Returns:
        str -- The script tag or an empty string.
    """

    if not DJANGO_VITE_DEV_MODE:
        return ""

    return f""" <script type="module">
        import RefreshRuntime from '{_generate_vite_server_url(DJANGO_VITE_REACT_HMR)}'
        RefreshRuntime.injectIntoGlobalHook(window)
        window.$RefreshReg$ = () => {{}}
        window.$RefreshSig$ = () => (type) => type
        window.__vite_plugin_react_preamble_installed__ = true
        </script>"""


@register.simple_tag
@mark_safe
def vite_hmr_injection() -> str:
    """
    Generates the script tag for the Vite WS client for HMR.
    Only used in development, in production this method returns
    an empty string.

    Returns:
        str -- The script tag or an empty string.
    """

    return generate_vite_ws_client()
