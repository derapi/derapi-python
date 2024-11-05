from typing import Any, Generator

import pytest

from derapi import Client
from derapi.api.sites import get_site, list_sites
from derapi.api.virtual import create_virtual_site, delete_virtual_site
from derapi.models.create_virtual_site_request import CreateVirtualSiteRequest
from derapi.models.create_virtual_site_response import CreateVirtualSiteResponse
from derapi.models.vendor import Vendor


@pytest.fixture(scope="module")
def virtual_site(virtual_client: Client) -> Generator[CreateVirtualSiteResponse, Any, Any]:
    virtual_site = create_virtual_site.sync(
        client=virtual_client,
        body=CreateVirtualSiteRequest(name="My test site"),
    )
    assert virtual_site is not None

    yield virtual_site

    delete_virtual_site.sync_detailed(virtual_site.id, client=virtual_client)


def test_get_site(virtual_client: Client, virtual_site: CreateVirtualSiteResponse) -> None:
    site = get_site.sync(virtual_site.id, client=virtual_client)
    assert site is not None

    assert site.name == "My test site"
    assert site.vendor == Vendor.VIRTUAL


def test_list_sites(virtual_client: Client, virtual_site: CreateVirtualSiteResponse) -> None:
    sites = list_sites.sync_depaginated(client=virtual_client)
    assert any(site.id == virtual_site.id for site in sites)
