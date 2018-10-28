from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

class HomePageView(TemplateView):
    template_name = "index.html"

class RecommendationsView(TemplateView):
    template_name = "anime.html"