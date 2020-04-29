from time import sleep
from prompts import get_bet

class Bets:


  # takes in a list of players and a starting bankroll for betting
  def __init__(self, p_list, start_money):
    self.p_list = p_list
    self.start_money = start_money
    self.bets_log = self.get_bets_log()


  # creates a dict for keeping count of each player's hands, bets and overall bankroll
  def get_bets_log(self):
    bets_log = [None]
    for p in self.p_list:
      bets_dict = {}
      bets_dict['Name'] = p
      bets_dict['Bankroll'] = self.start_money
      bets_dict['Current Hand'] = []
      bets_dict['Current Bet'] = 0
      bets_dict['Playing'] = True
      bets_log.append(bets_dict)

    return bets_log

  
  # prompts players to place bets, updates log
  def place_your_bets(self):
    print('\nGentlemen, please place your bets!')

    for p in self.bets_log[1:len(self.bets_log)-1]:
      player = p['Name']
      max_bet = p['Bankroll']
      bet = get_bet(self, player, max_bet)
      p['Current Bet'] = bet


  # returns True if there are active players    
  def check_statuses(self):
    for p in self.bets_log[1:len(self.bets_log)-1]:
      return True if p['Playing'] == True else False
  

  # resets all player status to True
  def update_status(self):
    for p in self.bets_log[1:len(self.bets_log)-1]:
      p['Playing'] = True

  

  