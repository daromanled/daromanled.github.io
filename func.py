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
    
