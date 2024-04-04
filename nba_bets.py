import pandas as pd 

#open files
#file1 = open('nba_player_data.txt', 'r')

file1 = open("nba_player_data.txt", encoding="utf8")
file2 = open('nba_defense 1.txt', encoding="utf8")

player_stats = file1.readlines()
team_stat = file2.readlines()
#print(team_stat)

nba_player = []
team_stats = []


for line in player_stats:
    nba_player.append(line)

for line2 in team_stat:
    team_stats.append(line2)

#print(team_stats)   
average_for_allpro = []
Combine_line = []
player_comparison = []
ideal_traits = []
defensive_rank = []
team_name = []
games_played = []
Wins =[]
losses=[]
minutes=[]
offensive_rating = []
defensive_rating =[]
Net_rating =[]
ast_percent =[]
ast/turnover =[]
ast_ratio =[]
offensive_rebound = []
defensive_rebound=[]
rebound_percent=[]
turnovers=[]
effiency
trus_shooting 
pace 
pie 
possesions

 'PACE', 'PIE', 'POSS'

for team in team_stats:
    team_stats = team.rstrip('\n').split('\t')
    print(team_stats)
    
    if (team_stats[0] == 'rk' ):
        continue
    
    defensive_rank= team_stats[0]
    team_name = team_stats[1]
    



