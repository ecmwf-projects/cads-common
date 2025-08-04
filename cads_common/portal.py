import os

# FIXME: this should be moved into the k8s configuration, as a yaml file into operator folder
# This still requires us to change the code when new portal are added
FALLBACK_PORTAL_URLS = {
    "c3s": "https://cds.climate.copernicus.eu",
    "cams": "https://ads.atmosphere.copernicus.eu",
    "cems": "https://ewds.climate.copernicus.eu",
    "eds": "https://eds.hub.copernicus.eu",
    "hds": "https://hds.hub.copernicus.eu",
}

PORTALS_TO_SITES = {
    "c3s": "cds",
    "cams": "ads",
    "cems": "ewds",
    "hds": "hds",
    "eds": "eds",
}


def get_site_url(portal: str) -> str | None:
    """Return the reference URL for a given site based on portal header value.

    This works based on environment variables specific for configure multiple portals that K8S
    spreads among pods.
    """
    site = PORTALS_TO_SITES.get(portal)
    if not site:
        return None
    return os.getenv(f"{site.upper()}_PROJECT_URL", FALLBACK_PORTAL_URLS.get(portal))
