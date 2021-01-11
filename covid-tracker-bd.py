import requests, datetime, pyrebase
from bs4 import BeautifulSoup

x = datetime.datetime.now()

date_ = x.strftime("%d")
month_ = x.strftime("%B")
year_ = x.strftime("%Y")
f_name = date_ + " " + month_  + " " + year_ + ".txt"
child_name = date_ + " " + month_  + " " + year_

URL = 'https://corona.gov.bd/lang/en'
headers = {
    "User-Agent":
    "YOUR_USER_AGENT_HERE"
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

msg = f"  {month_} {date_} ☆☆ [Bangladesh] \n [Infected] \n    Last 24 Hours = {*newly_infected,} \n    Total = {*total_infected,} \n [Deaths] \n    Last 24 Hours = {*dead_24,} \n    Total = {*dead_total,} \n [Cured] \n    Last 24 Hours = {*cure_24,} \n    Total = {*cure_total,} \n [Tests Taken] \n    Last 24 Hours = {*tests_24,} \n    Total = {*tests_total,}".replace('(', '').replace(')', '').replace("'", "").replace(",", "").strip()


# The below code is to save it to a file, you can un-comment it to use it 
'''
with open(f_name, "a", encoding="utf-8") as f:
    f.write(msg)
'''

# The below code is to save it to a firebase database

db_infected_new = f"{newly_infected}".replace("<b>", '').replace("</b>", '').strip()
db_infected_total = f"{total_infected}".replace("<b>", '').replace("</b>", '').strip()
    
db_dead_new = f"{dead_24}".replace("<b>", '').replace("</b>", '').strip()
db_dead_total = f"{dead_total}".replace("<b>", '').replace("</b>", '').strip()
    
db_cure_new = f"{cure_24}".replace("<b>", '').replace("</b>", '').strip()
db_cure_total = f"{cure_total}".replace("<b>", '').replace("</b>", '').strip()

db_tests_new = f"{tests_24}".replace("<b>", '').replace("</b>", '').strip()
db_tests_total = f"{tests_total}".replace("<b>", '').replace("</b>", '').strip()

firebaseConfig = {
    "YOUR_CONFIG_HERE"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
data = {
    "Infected (24hrs)": db_infected_new,
    "Infected (Total)": db_infected_total,
    "Deaths (24hrs)": db_dead_new,
    "Deaths (Total)": db_dead_total,
    "Cure (24hrs)": db_cure_new,
    "Cure (Total)": db_cure_total,
    "Tests (24hrs)": db_tests_new,
    "Tests (Total)": db_tests_total
}
db.child(child_name).set(data)
