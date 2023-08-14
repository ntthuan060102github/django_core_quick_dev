import json
import requests

def request(**kwargs):
    try:
        url = kwargs.get('url', None)
        data = kwargs.get('payload', None)
        params = kwargs.get('params', None)
        headers = kwargs.get('headers', None)
        method = kwargs.get('method', None)
        proxies = kwargs.get('proxies', None)

        return requests.request(
            method=method, 
            url=url, 
            params=params,
            data=json.dumps(data),
            headers=headers,
            proxies=proxies,
            verify=False
        ).json()

    except Exception as e:
        print(e)
        raise e
