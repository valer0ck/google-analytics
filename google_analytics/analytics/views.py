from django.shortcuts import render_to_response
from django.conf import settings
from .service_account import get_access_token


def analytics(request):
    """ Show google analytics without google login """

    token = get_access_token()
    view_id = settings.VIEW_ID
    template = "google_analytics.html"
    return render_to_response(template, locals())
