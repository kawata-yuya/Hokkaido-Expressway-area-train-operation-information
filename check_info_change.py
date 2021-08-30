import requests

def check(text, secret_url):
    payload = {'text': text}
    r = requests.get(secret_url, params=payload).json()

    return r['change']
