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
current_datetime_label = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# extract values
items = []
for grid in soup.find_all(class_="rate grid-x"):
    name = grid.find(class_="name").text
    rate = grid.find(class_="rate-percent").text
    try:
        fees = grid.find(class_="fees").text
    except:
        fees = "Fee not displayed"
    item = [name, rate, fees, current_datetime]
    items.append(item)

# save as dataframe
df = pd.DataFrame(items)
df.columns = ['name', 'rate', 'fees', 'datetime']

# export to csv
file_path = 'data/fm-rates-' + current_datetime_label + '.csv'
df.to_csv(file_path, index = False)
