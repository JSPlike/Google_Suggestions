import requests
from bs4 import BeautifulSoup

keyword = '박준영'
google_related_keyword_api = 'http://suggestqueries.google.com/complete/search?output=toolbar&q=' + keyword
response = requests.get(google_related_keyword_api)       
soup = BeautifulSoup(response.content, 'xml')                                                                 

datas1 = soup.select('suggestion')

for item in datas1:
    print(item['data'])
