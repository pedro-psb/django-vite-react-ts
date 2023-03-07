from django.urls import path

from .utils import render_react

urlpatterns = [
    # path("", template("index.html")),
    path("", render_react("pages/main.tsx")),
    path("about", render_react("pages/about.tsx", context={"name": "Pedro Pessoa"})),
]
