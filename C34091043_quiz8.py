import csv

# Helper functions to calculate win percentages
def calculate_pct(record):
    wins, losses = map(int, record.split('-')[:2])  # 只取前兩個部分來計算勝率
    return wins / (wins + losses)

# Load the CSV file
filename = "pe8_data.csv"  # 確保這裡是你的檔案名稱

teams = []

with open(filename, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Home_PCT'] = calculate_pct(row['HOME'])
        row['Away_PCT'] = calculate_pct(row['AWAY'])
        row['PF'] = float(row['PF'])
        row['PA'] = float(row['PA'])
        row['PF_minus_PA'] = row['PF'] - row['PA']
        teams.append(row)

# (1) Eastern Conference teams with Home win percentage lower than Away win percentage
east_teams = [team['Team'] for team in teams if team['Conference'] == 'Eastern' and team['Home_PCT'] < team['Away_PCT']]

# (2) Conference with higher average PF minus PA
east_pf_minus_pa = [team['PF_minus_PA'] for team in teams if team['Conference'] == 'Eastern']
west_pf_minus_pa = [team['PF_minus_PA'] for team in teams if team['Conference'] == 'Western']

avg_pf_minus_pa_east = sum(east_pf_minus_pa) / len(east_pf_minus_pa)
avg_pf_minus_pa_west = sum(west_pf_minus_pa) / len(west_pf_minus_pa)

higher_avg_pf_minus_pa_conference = 'Eastern' if avg_pf_minus_pa_east > avg_pf_minus_pa_west else 'Western'

# (3) Rank teams based on win percentage against the other conference
for team in teams:
    total_wins, total_losses = map(int, team['W-L'].split('-'))
    home_wins, home_losses = map(int, team['HOME'].split('-')[:2])
    away_wins, away_losses = map(int, team['AWAY'].split('-')[:2])
    team['W_other_conf'] = total_wins - (home_wins + away_wins)
    team['L_other_conf'] = total_losses - (home_losses + away_losses)
    total_other_conf_games = team['W_other_conf'] + team['L_other_conf']
    
    if total_other_conf_games > 0:
        team['other_conf_PCT'] = team['W_other_conf'] / total_other_conf_games
    else:
        team['other_conf_PCT'] = 0  # 如果沒有與另一區的比賽，設置勝率為0

ranked_teams = sorted(teams, key=lambda x: x['other_conf_PCT'], reverse=True)

# Display results
print("Teams from the Eastern Conference with Home win percentage lower than Away win percentage:")
for team in east_teams:
    print(team)

print(f"\nConference with higher average PF minus PA: {higher_avg_pf_minus_pa_conference}")

print("\nRanking of teams based on win percentage against the other conference:")
for idx, team in enumerate(ranked_teams, start=1):
    print(f"{idx}. {team['Team']}")
