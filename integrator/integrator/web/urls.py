"""
web url router
"""

from django.conf.urls import include, url

from .app_one import urls as app_one_urls


urlpatterns = [
    url(r'^app_one/', include(app_one_urls)),
]
