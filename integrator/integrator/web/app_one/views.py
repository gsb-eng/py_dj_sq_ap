from django.http import HttpResponse
"""
Sample view for appa_one
"""

import datetime


def app_one_home(request):
    now = datetime.datetime.now()
    html = "<html><body>Under construction</body></html>"
    # To Do: Add a simple template.
    return HttpResponse(html)
