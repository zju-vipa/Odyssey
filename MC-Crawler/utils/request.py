import requests
import time 
import random
def get_html_content(url: str) -> str:
    random_min = 1
    random_max = 5
    while True:
        # try until success because wiki anti spider methods
        if random_min < random_max:
            sleep_time = random.uniform(random_min, random_max)
        else:
            sleep_time = random_max
        try:
            response = requests.get(url)
            break
        except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:
            print(f'Error: {e}')
            time.sleep(sleep_time)
            random_min += 1
            continue
    return response.text