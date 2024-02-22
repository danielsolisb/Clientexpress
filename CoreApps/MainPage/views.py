
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, DetailView, View, FormView

# Create your views here.
def page_not_found404(request, exception):
    return render(request, '404.html')
class main(TemplateView):
    template_name = 'main.html'