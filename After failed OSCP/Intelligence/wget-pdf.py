import requests
import wget
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 1, 1)

current_date = start_date
while current_date < end_date:
    url = f'http://10.129.95.154/documents/{current_date.strftime("%Y-%m-%d")}-upload.pdf'
    response = requests.head(url)
    if response.status_code == 200:
        print(f"Downloading {url}")
        wget.download(url)
    current_date += timedelta(days=1)
