import requests
from bs4 import BeautifulSoup
import datetime

x = datetime.datetime.now()

date_ = x.strftime("%d")
month_ = x.strftime("%B")
year_ = x.strftime("%Y")
f_name = date_ + " " + month_  + " " + year_ + ".txt"

URL = 'https://corona.gov.bd/lang/en'
headers = {
    "User-Agent":
    'YOUR_USER_AGENT_HERE'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

b = []
b = soup('b', limit=12)

newly_infected = b[1]
total_infected = b[2]

dead_24 = b[4]
dead_total = b[5]

cure_24 = b[7]
cure_total = b[8]

tests_24 = b[10]
tests_total = b[11]

msg = f"☆☆  {month_} {date_} ☆☆ [Bangladesh] \n [Infected] \n    Last 24 Hours = {*newly_infected,} \n    Total = {*total_infected,} \n [Deaths] \n    Last 24 Hours = {*dead_24,} \n    Total = {*dead_total,} \n [Cured] \n    Last 24 Hours = {*cure_24,} \n    Total = {*cure_total,} \n [Tests Taken] \n    Last 24 Hours = {*tests_24,} \n    Total = {*tests_total,}"

msg.replace('(', '').replace(')', '').replace("'", "").replace(",", "").strip()

# The below code is to save it to a file, you can un-comment it to use it 
'''
with open(f_name, "a", encoding="utf-8") as f:
    f.write(msg)
'''