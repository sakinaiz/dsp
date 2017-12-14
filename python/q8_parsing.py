# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# Pre-work: Question 8
# Author: Sakina Zabuawala

import csv

with open("football.csv") as fid:
    reader = csv.reader(fid)
    team_goaldiff = {}
    next(reader, None)
    for row in reader:
        team_goaldiff[row[0]] = abs(int(row[5]) - int(row[6]))
        
    print('Team: ' + min(team_goaldiff, key=team_goaldiff.get))
    
#    min(team_goaldiff, key=lambda k: team_goaldiff.get(k) if team_goaldiff.get(k)>=0 else float("inf"))
        
    