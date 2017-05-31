from urllib.parse import urljoin
from pprint import pprint
import requests

AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'
APP_ID = '84cefc20ab794a7f9ff35b73c4146735'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

TOKEN = '9d0f75472c4242de8358755e1271e2f2'

class YandexMetrika(object):
    _METRIKA_STAT_URL = 'https://api-metrika.yandex.ru/stat/vl/'
    _METRIKA_MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/vl/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token),
            'User-Agent': 'netology.py3'
        }

    @property
    def counter_list(self):
        url = urljoin(self._METRIKA_MANAGEMENT_URL, 'counters')
        headers = self.get_header()
        response = requests.get(url, headers=headers)
        counter_list = [c['id'] for c in response.json()['counters']]
        return counter_list

    def get_visits_count(self, counter_id):
        url = urljoin(self._METRIKA_STAT_URL, 'data')
        headers = self.get_header()
        params = {
            'id': counter_id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(url, params, headers=headers)
        print(response.headers['Content-Type'])
        pprint(response.json())
        visits_count = response.json()['data'][0]['metrics'][0]
        return visits_count
