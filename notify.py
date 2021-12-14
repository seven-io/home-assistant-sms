"""Sms77 SMS for notify component."""
from http import HTTPStatus
import logging

import requests
import voluptuous as vol

from homeassistant.components.notify import PLATFORM_SCHEMA, BaseNotificationService
from homeassistant.const import (
    CONF_API_KEY,
    CONF_RECIPIENT,
    CONF_SENDER,
)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)
BASE_API_URL = "https://gateway.sms77.io/api/"
TIMEOUT = 5
PLATFORM_SCHEMA = vol.Schema(vol.All(PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_RECIPIENT, default=[]): vol.All(cv.ensure_list, [cv.string]),
    vol.Optional(CONF_SENDER, default="hass"): cv.string,
})))


def get_service(hass, config, discovery_info=None):
    """Get the Sms77 notification service."""
    if not _authenticate(config):
        _LOGGER.error("You are not authorized to access Sms77")
        return None
    return Sms77SmsNotificationService(config)


class Sms77SmsNotificationService(BaseNotificationService):
    """Implementation of a notification service for the Sms77 service."""

    def __init__(self, config):
        """Initialize the service."""
        self.api_key = config[CONF_API_KEY]
        self.recipients = config[CONF_RECIPIENT]
        self.sender = config[CONF_SENDER]

    def send_message(self, message="", **kwargs):
        """Send a message to a user."""
        res = requests.post(
            f"{BASE_API_URL}sms",
            data={
                "from": kwargs['data']['sender']
                if kwargs['data'] is not None and 'sender' in kwargs['data']
                else self.sender,
                "text": message,
                "to": ','.join(self.recipients),
            },
            headers=_build_headers(self.api_key),
            timeout=TIMEOUT,
        )

        if res.status_code == HTTPStatus.OK and (res.text == '100' or res.text == '101'):
            return

        _LOGGER.error("Error %s : (Code %s)", res.status_code, res.text)


def _authenticate(config):
    """Authenticate with Sms77."""
    res = requests.get(
        f"{BASE_API_URL}balance",
        headers=_build_headers(config[CONF_API_KEY]),
        timeout=TIMEOUT,
    )

    return res.status_code == HTTPStatus.OK and "." in res.text


def _build_headers(api_key, sent_with="home-assistant"):
    return {"X-Api-Key": api_key, "SentWith": sent_with}
