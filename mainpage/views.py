from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .forms import LoginForm

class HomePageView(TemplateView):
    template_name = "index.html"

class RecommendationsView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        return render(request, self.template_name, {'form': form, 'username': username,
                                                    'password': password})