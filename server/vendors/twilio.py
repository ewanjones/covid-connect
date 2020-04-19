from twilio.rest import Client


class TwilioClient:
    def __init__(self, sid: str, token: str, service_name: str):
        self.sid = sid
        self.token = token
        self.service_name = service_name
        self._client = Client(self.sid, self.token)

    def create_channel(self):
        return self._client.chat.services(self.service_name).channels.create()

    def get_channel(self, channel_sid):
        return (
            self._client.chat.services(self.service_name).channels(channel_sid).fetch()
        )

    def get_service(self, name: str):
        return self._client.chat.services.create(friendly_name=name)

    def _create_service(self, name: str):
        """
        Create a new service.

        Services represent different environments, so use this only if needed.
        """
        return self._client.chat.services.create(friendly_name=name)
