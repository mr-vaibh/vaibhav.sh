from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def path(request, path):
    return TemplateView.as_view(template_name='home/site_content/' + path)(request)