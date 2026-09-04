from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View



from .forms import SignUpForm, CustomLoginForm


class SignUpView(View):

    def get(self, request):
        form = SignUpForm()

        return render(
            request,
            "registration/signup.html",
            {"form": form}
        )

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

        return render(
            request,
            "registration/signup.html",
            {"form": form}
        )


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginForm