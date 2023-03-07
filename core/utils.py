from django.shortcuts import render


def render_react(react_filename: str, context: dict = {}):
    """
    Renders the react page component with the given context
    The root for the react filename is the configured static folder.
    """
    return lambda request: render(
        request,
        "react-page.html",
        context={"react_filename": react_filename, "context": context},
    )
