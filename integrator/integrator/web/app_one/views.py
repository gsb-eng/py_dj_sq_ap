from django.http import HttpResponse
"""
Sample view for appa_one
"""

import datetime


def app_one_home(request):
    now = datetime.datetime.now()
    return HttpResponse(now)
