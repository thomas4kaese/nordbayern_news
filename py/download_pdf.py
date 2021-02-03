import requests
import os
import platform
from datetime import datetime

# find out os
my_os = platform.system()

# run either sh or bat file
if my_os == 'Windows':
    os.system('nn2.bat')
elif my_os == 'Linux' or  my_os == 'Darwin':
    os.system('sh nn2.sh')
else:
    print('OS cannot be detected')
    raise ValueError('Cannot find out OS')

# read content of output file created by script
f = open("output.txt", "r").read()

# extract token by finding flanking strings
start = f.find("token=") + len("token=")
end = f.find(" was not found")
token = f[start:end]

# create datestamp for download of todays news
now = datetime.now()
date = now.strftime("%Y%m%d")

# download
site_download = 'https://e-paper.nordbayern.de/ee/nn/pdf/?page=download_full&device=pdf&date=' + date + '&edition=11&token=' + token + '&edname=Pegnitz%20Zeitung'

# write pdf
with requests.Session() as s:
    response = s.get(site_download)
    with open('zeitung_' + date + '.pdf', 'wb') as f:
        f.write(response.content)