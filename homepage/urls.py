from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("payments/pubkey/", views.get_stripe_pubkey, name="payments_pubkey"),
]
