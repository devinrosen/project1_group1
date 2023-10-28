from django.urls import path, re_path

from . import views

UUID_RE = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

urlpatterns = [
    path("", views.Portfolios.as_view(), name='portfolios'),
    re_path(f"^(?P<pk>{UUID_RE})/?$", views.Portfolio.as_view(), name="portfolio"), # NOQA
]