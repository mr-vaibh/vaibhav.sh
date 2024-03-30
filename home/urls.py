from django.urls import path

from django.views.generic import TemplateView
from . import views

app_name = 'home'
urlpatterns = [
    path("", TemplateView.as_view(template_name='home/index.html'), name="index"),
    path("resume", TemplateView.as_view(template_name='home/resume.html'), name="resume"),
    # Site content
    path("<path:path>", views.path, name="path"),
]