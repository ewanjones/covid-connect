from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView, TemplateView

from . import forms, models


class Login(LoginView):
    template_name = "login.html"
    success_url = "/"


class Logout(LogoutView):
    redirect_url = "/login"


class Register(FormView):
    template_name = "register.html"
    success_url = "/"
    form_class = forms.Register

    def form_valid(self, form):
        data = form.cleaned_data
        try:
            models.User.objects.create_user(
                data["email"],
                data["password"],
                data["full_name"],
                data["nickname"],
                data["phone"],
            )
        except Exception as e:
            form.add_error(None, str(e))
            return self.form_invalid()

        return self.get_success_url()


class Home(TemplateView):
    template_name = "home.html"
