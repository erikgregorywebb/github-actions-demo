import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# get page content
url = 'http://www.freddiemac.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# get current date and datetime
current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
current_date = datetime.now().strftime('%Y-%m-%d')

# extract values
items = []
for grid in soup.find_all(class_="rate grid-x"):
    name = grid.find(class_="name").text
    rate = grid.find(class_="rate-percent").text
    fees = grid.find(class_="fees").text
    item = [name, rate, fees, current_datetime]
    items.append(item)

# save as dataframe
df = pd.DataFrame(items)
df.columns = ['name', 'rate', 'fees', 'datetime']

# export to csv
file_path = 'data/freddiemac-rates-' + current_date + '.csv'
df.to_csv(file_path, index = False)
