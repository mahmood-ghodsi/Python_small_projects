import re
from bs4 import BeautifulSoup
import requests
myreq = requests.get('https://divar.ir/s/tehran')

soup = BeautifulSoup(myreq.text,'html.parser')
all_ads = soup.find_all('a',attrs={'class':'kt-post-card kt-post-card--outlined','class':'kt-post-card kt-post-card--outlined kt-post-card--has-chat'})
for ads in all_ads:
    if 'توافقی' in ads.text:
      print(re.sub(r'\s+',' ',ads.text).strip())
    else:
        continue
#kt-post-card--has-chat