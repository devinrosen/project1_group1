from django.urls import path, re_path

from . import views


TEXT_RE = "[a-zA-Z0-9]*"


urlpatterns = [
    path("", views.DataSources.as_view(), name='sources'),
    re_path(f"^(?P<source>{TEXT_RE})/?$", views.DataSource.as_view(), name="source"), # NOQA
    re_path(f"^(?P<source>{TEXT_RE})/(?P<series>{TEXT_RE})/?$", views.DataSeries.as_view(), name="series"), # NOQA
]
