import time, random, requests, traceback

USERNAME = 'your username'
API_TOKEN = 'your api token'

url = 'https://api.imgur.com/3/account/{}/settings'.format(USERNAME)
headers = {'Authorization': 'Bearer {}'.format(API_TOKEN)}

while True:
    try:
        with open("lines.txt") as f:
            lines = [l.rstrip() for l in f]
            parameters = {'bio': random.choice(lines)}
            response = requests.put(url, headers=headers, params=parameters)
        print('Updated Imgur Bio!')
        time.sleep(300)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
