# mainpage/urls.py

from django.conf.urls import url
from mainpage import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
]