import os
from unittest.mock import patch

import pytest

from cads_common.portal import FALLBACK_PORTAL_URLS, PORTALS_TO_SITES, get_site_url


def test_get_site_url_with_valid_portal_and_env_var():
    """Test get_site_url with valid portal and environment variable set."""
    with patch.dict(os.environ, {"CDS_PROJECT_URL": "https://test-cds.example.com"}):
        result = get_site_url("c3s")
        assert result == "https://test-cds.example.com"


def test_get_site_url_with_valid_portal_no_env_var():
    """Test get_site_url with valid portal but no environment variable."""
    # Ensure the environment variable is not set
    with patch.dict(os.environ, {}, clear=True):
        result = get_site_url("c3s")
        assert result == FALLBACK_PORTAL_URLS["c3s"]


def test_get_site_url_with_invalid_portal():
    """Test get_site_url with invalid portal returns None."""
    result = get_site_url("invalid_portal")
    assert result is None


def test_get_site_url_empty_portal():
    """Test get_site_url with empty string portal."""
    result = get_site_url("")

    assert result is None


@pytest.mark.parametrize(
    "portal,expected_site",
    [
        ("c3s", "cds"),
        ("cams", "ads"),
        ("cems", "ewds"),
        ("eds", "eds"),
        ("hds", "hds"),
    ],
)
def test_portal_to_site_mapping(portal, expected_site):
    """Test that portal to site mapping is correct."""
    assert PORTALS_TO_SITES[portal] == expected_site


def test_environment_variable_precedence():
    """Test that environment variables take precedence over fallback URLs."""
    test_url = "https://custom-environment.example.com"
    with patch.dict(os.environ, {"CDS_PROJECT_URL": test_url}):
        result = get_site_url("c3s")
        assert result == test_url
        assert result != FALLBACK_PORTAL_URLS["c3s"]
