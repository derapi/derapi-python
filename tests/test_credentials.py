import random

from derapi.api.vendor_credentials import create_vendor_credentials, delete_vendor_credentials
from derapi.client import Client
from derapi.models.create_vendor_credentials_request import CreateVendorCredentialsRequest
from derapi.models.enphase_partner_app_credentials import EnphasePartnerAppCredentials
from derapi.models.hidden_enphase_partner_app_credentials import HiddenEnphasePartnerAppCredentials


def test_create_credentials(client: Client):
    credentials = create_vendor_credentials.sync(
        client=client,
        body=CreateVendorCredentialsRequest(
            name="hi",
            credentials=EnphasePartnerAppCredentials(
                client_id="client_id",
                client_secret="".join(random.sample("abcdefghijklmnopqrstuvwxyz", 10)),
                api_key="api_key",
            ),
        ),
    )
    assert credentials is not None
    assert isinstance(credentials.credentials, HiddenEnphasePartnerAppCredentials)

    delete_vendor_credentials.sync_detailed(credentials.id, client=client)
