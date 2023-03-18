import matplotlib.pyplot as pyplot
from football_players_exploration import *

def caps_and_goals(position):
    caps = []
    goals = []
    exploration = FootballPlayersExploration('football/football_players_exploration.db')
    players = exploration.session.query(Player).filter(Player.position==position).all()
    for player in players:
        caps.append(player.caps)
        goals.append(player.goals)
    
    return caps, goals
    
def make_scatter_plot(position):
    caps, goals = caps_and_goals(position)
    pyplot.scatter(caps, goals)
    pyplot.show()

    
if __name__ == '__main__':
    make_scatter_plot(position='FW')
    make_scatter_plot(position='MF')
    make_scatter_plot(position='DF')
    make_scatter_plot(position='GK')





