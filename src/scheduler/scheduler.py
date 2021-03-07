import requests
from .models import Scheduler


def _get_request_json(base_url):
    r = requests.get(base_url)
    return r.status_code


def schedule(*args):
    url = args[0]['url']
    pk = args[1]
    json = _get_request_json(url)
    if json == 200:
        try:
            Scheduler.objects.filter(pk=pk).update(status='Completed', result=json)
        except:
            pass