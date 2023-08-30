'''AUTHS VIEWS'''
#Django
from django.shortcuts import render
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse

#local
from auths.forms.registeg_form import RegisterForm

# Create your views here.

class LoginView(View):
    """
    User login.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        ...

    def post(self, request: HttpRequest) -> HttpResponse:
        ...


class RegisterView(View):
    """
    User Register.
    """
    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form' : form
            }
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        breakpoint()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form' : form
            }
        )