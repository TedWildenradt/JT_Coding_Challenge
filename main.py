import time
class Soccer(object):
  def __init__(self):
    self.played = set()
    self.teams = {} 
    self.day = 0

  def parseTeamAndScore(self,team):
    team = team.strip()
    i = len(team) - 1
    while True:
      if team[i].isdigit() or team[i] == ' ':
        i -= 1
      else:
        break
    team_name = team[:i+1]
    # I'm just going to assume no one scores more than 9 goals per team.
    score = team[-1]
    return[team_name,score]

  def rankScoreboard(self, dic):
    # first sort by alphabet (for tiebreakers), then by point totals
    ordered_alpha = sorted(self.teams.items(), key=lambda x: x[0])
    return sorted(ordered_alpha, key=lambda x: x[1], reverse=True)[:3]
  
  def printScores(self):
    self.day += 1
    print('Matchday ' + str(self.day))
    top_teams = self.rankScoreboard(self.teams)
    for team in top_teams:
      if team[1] == 1:
        points = "pt"
      else:
        points = "pts"
      print(team[0] + ", " + str(team[1]) + " " + points)
    print('\n')

  def determinePoints(self,team1,team2):
    team1,team1_score = team1
    team2,team2_score = team2

    team1_points = team2_points = 0

    if team1_score > team2_score:
      team1_points = 3
    elif team1_score < team2_score:
      team2_points = 3
    else:
      team1_points = team2_points = 1

    # This determines whether we are in a new matchday
    if team1 in self.played or team2 in self.played:
      self.printScores()
      time.sleep(1)
      self.played = set() 

    # update team point totals
    self.teams[team1] = self.teams.get(team1,0) + team1_points
    self.teams[team2] = self.teams.get(team2,0) + team2_points

    self.played.add(team1)
    self.played.add(team2)

  def script(self):
    file_pathway = input('Enter a file pathway: ')
    try:
      file_object = open(file_pathway,'r')
    except:
      print('Sorry, that file cannot be found. Please try again.')
      return
    for line in file_object:
      game = line.split(',')
      if len(game) != 2:
        print('Error. The line: "' + line + '" is not in the form expected')
        return
      team1_info = self.parseTeamAndScore(game[0])
      team2_info = self.parseTeamAndScore(game[1])
      self.determinePoints(team1_info,team2_info)
    file_object.close()
    self.printScores()

if __name__ == "__main__":
  soccer = Soccer()
  soccer.script()
