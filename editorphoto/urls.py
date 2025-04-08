from django.urls import path
from .views import editor_page, upload_image, list_images, black_and_white, add_watermark_view



urlpatterns = [
    path("", editor_page, name="editor-page"),
    path('upload/', upload_image, name='upload'),
    path('images/', list_images, name='list'),
    path('bw/<int:image_id>/', black_and_white, name='bw'),
    path('watermark/<int:image_id>/', add_watermark_view, name='watermark'),
]
