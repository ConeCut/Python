import pandas as pd

data = pd.read_csv('dataset.csv')

arsenal_data = data[data['Club'] == 'Arsenal']

top_scorers_arsenal = arsenal_data[['Name', 'Goals']].sort_values(by='Goals', ascending=False).head(5)
print("Topp 5 målscorere i Arsenal:")
print(top_scorers_arsenal)

defenders_arsenal = arsenal_data[arsenal_data['Position'] == 'Defender']
top_defenders_arsenal = defenders_arsenal[['Name', 'Yellow cards']].sort_values(by='Yellow cards', ascending=False).head(5)
print("\nTopp 5 forsvarere i Arsenal etter gule kort:")
print(top_defenders_arsenal)

goalkeepers_arsenal = arsenal_data[arsenal_data['Position'] == 'Goalkeeper']
top_goalkeepers_arsenal = goalkeepers_arsenal[['Name', 'High Claims', 'Catches']].sort_values(by='High Claims', ascending=False).head(5)
print("\nMålvakter i Arsenal med flest 'High Claims' og 'Catches':")
print(top_goalkeepers_arsenal)

avg_age_arsenal = arsenal_data['Age'].mean()
print(f"\nGjennomsnittsalderen på Arsenal-spillere: {avg_age_arsenal:.1f} år")