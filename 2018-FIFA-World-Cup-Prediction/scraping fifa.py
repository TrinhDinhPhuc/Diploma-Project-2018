# loading required packages
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
 
# initializing needed variables
fifa_url = 'https://www.fifa.com/fifa-world-ranking/ranking-table/men/rank={}/index.html'
first_page = 2
last_page = 287
list_downloaded_page = []
full_data = []
 
# launching chrome webdriver
driver = webdriver.Chrome()
 
try:
   for i in range(first_page, last_page+1):
      target_url = fifa_url.format(i)
      driver.get(target_url)
      time.sleep(10)
      driver.find_element_by_link_text('201-211').click()
      time.sleep(3)
      soup = BeautifulSoup(driver.page_source, 'html.parser')
      time.sleep(1)
      rank_date = soup.find('div', {'class':['slider-wrap']}).find('li').text.strip()
      rank_date = datetime.datetime.strptime(rank_date, '%d %B %Y')
 
      for table in soup.find_all('table', 'table tbl-ranking table-striped'):
         for tr in table.find_all('tr', 'anchor'):
            row_data = []
            for td in tr.find_all('td'):
               try:
                  res = td.text.strip()
                  row_data += [res]
               except TypeError:
                  pass
            row_data += [rank_date]
            full_data.append(row_data) 
finally:
   driver.quit()
fifa_rank = pd.DataFrame(full_data)
fifa_rank.to_csv('fifa_ranking.csv', index=False, encoding='utf-8')
