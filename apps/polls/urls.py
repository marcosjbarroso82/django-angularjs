from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^poll/', views.PollView.as_view()),
]