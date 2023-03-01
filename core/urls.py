from django.urls import path
from django.views.generic import TemplateView as T


def template(file: str):
    return T.as_view(template_name=file)


urlpatterns = [
    path("", template("index.html")),
    path("about", template("about.html")),
]
