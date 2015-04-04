"""
app_one url's.
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.app_one_home),
]
