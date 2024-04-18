import os
import requests
import datetime
import subprocess

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2023, 1, 1)
base_url = 'http://10.129.95.154/documents/'

dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

for date in dates:
    url = f'{base_url}{date.strftime("%Y-%m-%d")}-upload.pdf'
    response = requests.head(url)
    if response.status_code == 200:
        filename = url.split('/')[-1]
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        creator = subprocess.check_output(['exiftool', '-Creator', filename])
        print(f'File {filename} downloaded. Creator: {creator.decode()}')
        os.remove(filename)
