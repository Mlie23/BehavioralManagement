"""mosaic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from dj_rest_auth.registration.views import VerifyEmailView #ConfirmEmailView
from allauth.account.views import ConfirmEmailView
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import VerifyEmailView
# from django.template.loader import render_to_string
# from django.core.mail import EmailMultiAlternatives

# class CustomVerifyEmailView(VerifyEmailView):
#     email_template_name = 'path/to/custom_email_template.html'

#     def send_mail(self, email, context):
#         subject = render_to_string('path/to/custom_email_subject.txt', context)
#         message = render_to_string(self.email_template_name, context)
#         email_message = EmailMultiAlternatives(subject, message, None, [email])
#         email_message.attach_alternative(message, 'text/html')
#         email_message.send()
        
urlpatterns = [
    path("admin/", admin.site.urls),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        'dj-rest-auth/registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
        name='account_confirm_email'
    ) , # needs to be defined before registration
    re_path(r'^account/', include('allauth.urls')),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        'dj-rest-auth/account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path("api/prism/", include("questionnaire.urls")),
    path("change-password/", auth_views.PasswordChangeView.as_view()),
    re_path(r'^', include('django.contrib.auth.urls')),
]
