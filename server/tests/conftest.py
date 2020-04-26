import django_webtest
import pytest
from django.urls import reverse

from tests import factories


class WebtestAppWrapper(object):
    """
    Wrapper class for the Webtest client to add some convenience methods.
    """

    OK = "200 OK"
    FOUND = "302 Found"

    # We keep a property reference to the user that we are masquerading as
    user = None

    def __init__(self, app):
        self.app = app

    def get(self, url_name=None, url_kwargs=None, **kwargs):
        if url_name is not None:
            url = reverse(url_name, kwargs=url_kwargs)
        else:
            url = kwargs.pop("url")

        return self.app.get(url, **kwargs)

    def post(self, url_name=None, url_kwargs=None, **kwargs):
        if url_name is not None:
            url = reverse(url_name, kwargs=url_kwargs)
        else:
            url = kwargs.pop("url")
        return self.app.post(url, **kwargs)

    def post_json(self, url_name=None, url_kwargs=None, **kwargs):
        if url_name is not None:
            url = reverse(url_name, kwargs=url_kwargs)
        else:
            url = kwargs.pop("url")
        return self.app.post_json(url, **kwargs)

    def set_user(self, user):
        self.user = user
        self.app.extra_environ["WEBTEST_USER"] = str(user.email)
        return self


@pytest.fixture
def anon_webapp():
    """
    Provide an API to interact with Django views.
    """
    app = django_webtest.DjangoTestApp()
    return WebtestAppWrapper(app)


@pytest.fixture
def auth_webapp():
    user = factories.User()
    app = django_webtest.DjangoTestApp()
    app.extra_environ["WEBTEST_USER"] = user.email
    return WebtestAppWrapper(app)


@pytest.fixture
def factory():
    """
    Provide a fixture to allow easy access to factories.
    """
    return factories
