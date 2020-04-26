import pytest


@pytest.mark.django_db
class TestLogin:
    def test_no_user_redirects_to_login(self, anon_webapp):
        response = anon_webapp.get("home")

        assert response.status == anon_webapp.FOUND
        assert "login" in response.url

    def test_user_can_login(self, anon_webapp, factory):
        user = factory.User()
        user.set_password("test")

        login_page = anon_webapp.get("login")
        form = login_page.form
        form["username"] = user.email
        form["password"] = "test"
        response = form.submit()

        # Assert we are redirected to home
        assert response.status == anon_webapp.OK
        assert response.url == b""

    def test_incorrect_credentials(self, anon_webapp, factory):
        user = factory.User()
        user.set_password("test")

        login_page = anon_webapp.get("login")
        form = login_page.form
        form["username"] = user.email
        form["password"] = "wrongpassword"
        response = form.submit()

        # Assert we are redirected to home
        assert response.status == anon_webapp.OK
        assert b"Please enter a correct email and password" in response.content


@pytest.mark.django_db
class TestRegister:
    def test_register_account_successfully(self, factory, anon_webapp):
        register_page = anon_webapp.get("register")
        form = register_page.form

        form["full_name"] = "someone"
        form["nickname"] = "someone"
        form["email"] = "someone@example.com"
        form["phone"] = "07123456789"
        form["password"] = "320dwekljrh3"
        response = form.submit()

        print(response.content)
        assert response.status == anon_webapp.FOUND
        assert "/" in response.url

    def test_register_missing_password(self, factory, anon_webapp):
        register_page = anon_webapp.get("register")
        form = register_page.form

        form["full_name"] = "someone"
        form["nickname"] = "someone"
        form["email"] = "someone@example.com"
        form["phone"] = "07123456789"
        form["password"] = ""
        response = form.submit()

        assert response.status == anon_webapp.OK

    def test_user_already_exists(self, factory, anon_webapp):
        user = factory.User()

        register_page = anon_webapp.get("register")
        form = register_page.form

        form["full_name"] = user.full_name
        form["nickname"] = user.nickname
        form["email"] = user.email
        form["phone"] = user.phone
        form["password"] = "something"
        response = form.submit()

        assert response.status == anon_webapp.OK


@pytest.mark.django_db
class TestLogout:
    def test_logout_sucessfully(self, factory, auth_webapp):
        response = auth_webapp.get("logout")

        assert response.status == auth_webapp.FOUND
        assert response.url == "/login"
