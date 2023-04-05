from django.urls import path
from django.views.generic import TemplateView
from .views import WebhookListener

urlpatterns = [
    # Directly calling the template since I'll be using Vue CDN to handle the front end
    path('', TemplateView.as_view(template_name="Mandrill/index.html")),

    # This is the endpoint that Mandrill will be sending the webhook to
    path('webhook/', WebhookListener.as_view(), name='webhook'),
]
