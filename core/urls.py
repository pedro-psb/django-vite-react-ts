from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView as T


def template(file: str):
    return T.as_view(template_name=file)


def about_page(request):
    return render(request, "about.html", context={"context": {"name": "Pedro"}})


urlpatterns = [
    path("", template("index.html")),
    path("about", about_page),
]
