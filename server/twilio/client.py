import requests
from django.conf import settings


class TwilioClient:
    def __init__(self, auth_token):
        self.base_url = settings.TWILLIO_BASE_URL + "Services"
        self.auth = (settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def make_call(self):
        pass
