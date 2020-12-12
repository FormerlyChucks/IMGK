import time, config, random, requests, traceback

url = 'https://api.imgur.com/3/account/<username>/settings'
headers = {'Authorization': 'Bearer <token>'}

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
