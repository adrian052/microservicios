import requests
import json
import codecs


def get_request(url,auth_key=None):
    headers = {'Authorization':auth_key}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.json()


def post_request(url, params={},auth_key=None):
    headers = {'Authorization':auth_key,
                'Content-Type':'application/json'}
    response = requests.post(url, data=params,headers=headers)
    content = response.content
    content_str = content.decode('utf-8')
    if response.status_code > 200 and response.status_code <300:
        return json.loads(content_str)

