from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("payments/pubkey/", views.get_stripe_pubkey, name="payments_pubkey"),
    path("all inclusive/", views.type_inclusive, name="all-inclusive"),
    path("half broad", views.type_half_broad, name="half-broad"),
    path("full broad", views.type_full_broad, name="full-broad"),
    path("bed breakfast", views.type_bed_breakfast, name="bed-breakfast"),
    path("add/", views.add_interval_time, name="interval"),
    path("interval_time/", views.interval_time, name="interval-time"),
]
