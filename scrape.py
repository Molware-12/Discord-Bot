from bs4 import BeautifulSoup
import requests
import logging
import re

class Scrape:
    def __init__(self, site, file):
        self.file = file
        self.site = site
    def html_site(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        h = requests.post(self.site, headers=headers)
        logging.log(20,h.text)
    def scrape(self):
        team_array = []  # Initialize empty list to store dictionaries for each team

        with open(self.file, "r") as f:
            tm = BeautifulSoup(f, "html.parser")
            tm.prettify()

            # Find the table containing the data for each team
            table = tm.find("table", class_="items")

            # Find all rows in the table
            rows = table.find_all("tr", class_=["odd", "even"])

            for row in rows:
                # Initialize dictionary which holds the keys of the data and empty strings which we will add the data onto
                team_stats = {"team": "", "league": "", "squad_value": "", "squad_size": "", "current_value": "", "current_size": "", "difference": "", "%": ""}

                # Extract data from each cell in the row
                cells = row.find_all("td")
                # Start from index 2 because the first 2 indexes are not going to be used
                team_stats["team"] = cells[2].text.strip()
                team_stats["league"] = cells[3].text.strip()
                team_stats["squad_value"] = cells[4].text.strip()
                team_stats["squad_size"] = cells[5].text.strip()
                team_stats["current_value"] = cells[6].text.strip()
                team_stats["current_size"] = cells[7].text.strip()
                team_stats["difference"] = cells[8].text.strip()
                team_stats["%"] = cells[9].text.strip()

                # Append the team_stats dictionary to team_array
                team_array.append(team_stats)

        return team_array
    
    def comparison(self, flag, team_name):
        data = self.scrape()
        
        for team in data:
            if team_name == team["team"] or team_name.lower() == team["team"].lower():
                if flag == "-sv":
                    return f"{team_name}'s Squad value as of 2023-12-15 = {team['squad_value']}"
                elif flag == "-ss":
                    return f"{team_name}'s Squad size as of 2023-12-15 = {team['squad_size']}"
                elif flag == "-cv":
                    return f"{team_name}'s Current value of squad = {team['current_value']}"
                elif flag == "-cs":
                    return f"{team_name}'s Current size of squad = {team['current_size']}"
                elif flag == "-d":
                    return f"{team_name}'s Difference of squad value as of 2023-12-15 and the current squad value = {team['difference']}"
                elif flag == "-p":
                    return f"{team_name}'s Percentage of the difference of squad value as of 2023-12-15 and the current squad value = {team['%']}"
    
    # Return a message if the team_name is not found in the data
        return f"Team '{team_name}' not found in the data."
h = Scrape("https://www.transfermarkt.us/premier-league/marktwerteverein/wettbewerb/GB1/stichtag/2023-12-15/plus/1", "transfermarkt.sc")
logging.basicConfig(level=20,filename=h.file, filemode="w")
h.html_site()
