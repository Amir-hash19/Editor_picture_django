from django.urls import path
from .views import editor_page


urlpatterns = [
    path("", editor_page, name="editor-page"),
]
