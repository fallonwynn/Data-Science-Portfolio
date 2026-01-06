import requests
import pandas as pd


#API to scrape NBA stats leaders site
url = "https://stats.nba.com/stats/leagueleaders"


#set header for API
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
    "Connection": "keep-alive",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true"
}

#Set parameters for API
params = {
    "LeagueID": "00",
    "PerMode": "PerGame",
    "Scope": "S",
    "Season": "2025-26",
    "SeasonType": "Regular Season",
    "StatCategory": "PTS"
}
#Send API request to access website and get data
response = requests.get(url, headers=headers, params=params)
data = response.json()

#Extract headers and rows from table
headers = data["resultSet"]["headers"]
rows = data["resultSet"]["rowSet"]

#Create dataframe
df = pd.DataFrame(rows, columns=headers)

print(df.head())
#create and save data as a csv file
df.to_csv("nba_stats_all_leaders_25_26.csv", index=False)
