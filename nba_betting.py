import pandas as pd 


team_stats = pd.read_csv("nba_defense 1.txt", sep="\t")

player_stats = pd.read_csv("nba_player_data.txt", sep=",")

filter_team1,filter_team2 = input('Enter the two teams (seperated by comma) that are playing: ').split(",")

filtered_teams=(team_stats.loc[team_stats['TEAM'] == filter_team1])
filtered_teams2 = (team_stats.loc[team_stats['TEAM'] == filter_team2])

print(player_stats)

info_dict = {
    "WAS": "Washington Wizards",
    "UTA": "Utah Jazz",
    "DET": "Detroit Pistons",
    "CHO":"Charlotte Hornets",
    
    "ATL": "Atlanta Hawks",
    "TOT": "Toronto Raptors",
    "DAL": "Dallas Mavericks",
    "POR": "Portland Trail Blazers",
    
    "SAC": "Sacramento Kings",
    "BRK": "Brooklyn Nets",
    "CHI": "Chicago Bulls",
    "LAL": "Los Angeles Lakers",
    
    "MIL": "Milwaukee Bucks",
    "GSW": "Golden State Warriors",
    "LAC": "LA Clippers",
    "PHO": "Phoenix Suns",
    
    "PHI": "Philadelphia 76ers",
    "MEM": "Memphis Grizzlies",
    "DEN": "Denver Nuggets",
    "MIA": "Miami Heat",
    
    "HOU": "Houston Rockets",
    "NYK": "New York Knicks",
    "NOP": "New Orleans Pelicans",
    "OKC": "Oklahoma City Thunder",
    
    "ORL": "Orlando Magic",
    "CLE": "Cleveland Cavaliers",
    "BOS": "Boston Celtics",
    "MIN": "Minnesota Timberwolves",
    "IND": "Indiana Pacers"
    
  }

#player_team1 = info_dict.keys()[info_dict.values().index(filter_team1)]  
#Newplayer_team2 = info_dict.keys()[info_dict.values().index(filter_team2)]

player_team1 = list(info_dict.keys())[list(info_dict.values()).index(filter_team1)]
player_team2 = list(info_dict.keys())[list(info_dict.values()).index(filter_team2)]

filtered_player1 = (player_stats.loc[player_stats['Tm'] == player_team1])

filtered_player2 = (player_stats.loc[player_stats['Tm'] == player_team2])

#print(filtered_player1,filtered_player2)

#filtered_player1.to_csv("nba bets info", sep='\t')
#afiltered_player2.to_csv("nba bets info2", sep='\t')


#filtered_teams  = (team_stats.loc[team_stats['TEAM'] == filter_team1])
#filtered_teams2 = (team_stats.loc[team_stats['TEAM'] == filter_team2])

list_of_dfs = []
list_of_dfs1 = []

list_of_dfs1.append(filtered_teams)
list_of_dfs1.append(filtered_teams2)
list_of_dfs.append(filtered_player1)
list_of_dfs.append(filtered_player2)


with open('nbabet_teams.txt', 'w', encoding="utf-8") as f:
    for w in list_of_dfs1:
        w.to_csv(f)
        f.write('\n')
        
with open('nbabet_players.txt', 'w', encoding="utf-8") as f:
    for w in list_of_dfs:
        
        w.to_csv(f)
        f.write('\n')
        f.write('\n')
        f.write('\n')


#print(filtered_teams,filtered_teams2)
#print(player_stats)

#print(filtered_player1)
#DAprint(filtered_player2)
