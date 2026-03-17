import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("matches.csv")

# Clean column names (PRO move)
df.columns = df.columns.str.strip().str.lower()

# Clean data
df = df.dropna(subset=['winner'])

# -----------------------------
# Create Season from Date (FIX 🔥)
# -----------------------------
df['date'] = pd.to_datetime(df['date'])
df['season'] = df['date'].dt.year

# -----------------------------
# Top 5 Teams by Wins
# -----------------------------
wins = df['winner'].value_counts().head(5)

print("\nTop 5 Teams by Wins:")
print(wins)

wins.plot(kind='bar')
plt.title("Top 5 IPL Teams by Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Toss Impact
# -----------------------------
toss_win_match_win = df[df['toss_winner'] == df['winner']]
percentage = (len(toss_win_match_win) / len(df)) * 100

print(f"\nToss winner also won match: {percentage:.2f}%")

# -----------------------------
# Matches per Season
# -----------------------------
season_count = df['season'].value_counts().sort_index()

season_count.plot(kind='line')
plt.title("Matches per IPL Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.show()

# -----------------------------
# Top Players of the Match
# -----------------------------
top_players = df['player_of_match'].value_counts().head(5)

top_players.plot(kind='bar')
plt.title("Top Player of the Match Winners")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Win Percentage (ELITE FEATURE 😏)
# -----------------------------
matches_played = pd.concat([df['team1'], df['team2']]).value_counts()
matches_won = df['winner'].value_counts()

win_percentage = (matches_won / matches_played) * 100
win_percentage = win_percentage.sort_values(ascending=False).head(5)

print("\nTop Teams by Win Percentage:")
print(win_percentage)

win_percentage.plot(kind='bar')
plt.title("Top Teams by Win Percentage")
plt.ylabel("Win %")
plt.xticks(rotation=45)
plt.show()