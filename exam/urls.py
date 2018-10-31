# helloworld/urls.py
from django.conf.urls import url
from exam.views.login import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
