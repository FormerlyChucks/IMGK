import time, config, random, requests, traceback

while True:
    try:
        with open("lines.txt") as f:
            response = requests.put(config.url, headers=config.headers, params={'bio': random.choice([l.rstrip() for l in f])})
        print('Updated Imgur Bio!')
        time.sleep(300)
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
