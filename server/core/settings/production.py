import os

from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["server", "localhost"]


STATIC_URL = "static/"
REACT_BUNDLE_BASE_URL = STATIC_URL + "bundle.js"

TWILIO_SERVICE_NAME = "LOCAL"
