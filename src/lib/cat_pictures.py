# http://random.cat/meow
# http:\/\/random.cat\/i\/066_-_0jJbuqA.gif

def cron(channel):
    import requests
    import json
    url = "http://random.cat/meow"
    resp = requests.get(url=url)
    data = json.loads(resp.content)  # creates a dict from json
    return data["file"].replace("\\", "")
