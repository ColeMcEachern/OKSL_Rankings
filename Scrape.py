from bs4 import BeautifulSoup
import requests
import json

WEBSITE = "https://braacket.com"

response = requests.get("https://braacket.com/league/oksl2022sfv/ranking?rows=200")

sfv_bracket_page = response.text

soup= BeautifulSoup(sfv_bracket_page, "html.parser")

player_names = []
player_profile_links =[]
player_points = []
player_ranks = []

data = soup.find_all(name="td", class_="ellipsis")
del data[0]
del data[-1]

for row in data:
    text = row.getText()
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    text = text.replace('\xa0', '')
    player_names.append(text)
    link = WEBSITE+row.contents[1].get("href")
    player_profile_links.append(link)
    player_ranks.append(data.index(row) + 1)

data_points = soup.find_all(name="td", class_="min text-right")

for row in data_points:
    player_points.append(int(row.getText()))



# print(player_ranks)
# print(player_names)
# print(player_points)
# print(player_profile_links)



data = {"players":[]}

for num in player_ranks:
    data["players"].append({"rank": num, "name": player_names[num-1], "points": player_points[num-1], "profileLink": player_profile_links[num-1]})

#
# json_string = json.dumps(data)
#
# with open('player_data.json', 'w') as outfile:
#     json.dump(json_string, outfile)

with open("player_data.json", "r") as f:
    d = json.load(f)
    print(d)

