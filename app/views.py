from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView

# Create your views here.
class home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'



