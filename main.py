from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#website to be scraped
url = "https://www.nba.com/stats/leaders"
#access the website
driver.get(url)

# Get page source AFTER JS loads
html = driver.page_source

#parse data
soup = BeautifulSoup(html, "html.parser")

#find table containing stats
table = soup.find("table", class_="Crom_table__p1iZz")

# Extract headers
headers = [th.text.strip() for th in table.find("thead").find_all("th")]

# Extract rows
rows = []
for tr in table.find("tbody").find_all("tr"):
    cells = [td.text.strip() for td in tr.find_all("td")]
    rows.append(cells)

# Create DataFrame
df = pd.DataFrame(rows, columns=headers)
print(df.head())

#create and save csv file
df.to_csv("nba_leaders.csv", index=False)

