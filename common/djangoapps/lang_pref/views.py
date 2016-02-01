"""
Language Preference Views
"""
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import LANGUAGE_SESSION_KEY
from lang_pref import LANGUAGE_KEY
from django.views.decorators.http import require_POST
from django.http import HttpResponse


@csrf_exempt
def update_language_session(request):
    """
    Update the language session key.
    """
    if request.method == 'PATCH':
        # Setting the session language to the browser language, if it is supported.
        data = json.loads(request.body)
        language = data.get(LANGUAGE_KEY, settings.LANGUAGE_CODE)
        if request.session.get(LANGUAGE_SESSION_KEY, None) != language:
            request.session[LANGUAGE_SESSION_KEY] = unicode(language)
    return HttpResponse(200)
