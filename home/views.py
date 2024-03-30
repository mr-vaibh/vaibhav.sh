from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def path(request, path):
    return TemplateView.as_view(template_name='home/site_content/' + path)(request)