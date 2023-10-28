from django.urls import path, re_path

from . import views


TEXT_RE = "[a-zA-Z0-9]*"


urlpatterns = [
    re_path(f"^(?P<series>{TEXT_RE})/?$", views.Series.as_view(), name="series"), # NOQA
]
