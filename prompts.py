from time import sleep

# initial start game prompt
def game_on():

  
  q = 'Press Y for yes and N for no\n'

  while True:

    start = input(q).upper()

    if start == 'Y':
      return True
    
    if start == 'N':
      return False
    
    else:
      continue


# prompts user to get number of players, returns a list of those players
def get_players():
  #p_list = [None]
  not_valid = '\nYou must enter a number between 1 and 5'
  
  while True:
    sleep(0.4)

    try:
      n_players = int(input('\nHow many players will be joining us?\n'))
    except ValueError:
      print(not_valid) 
      continue

    if n_players not in range(1, 6):
      print(not_valid)
      continue
    else:
      break

  return ['Player {}'.format(n) for n in range(1, n_players + 1)] + ['Dealer']


# prompts user to chose between 3 options for the starting bankroll
def get_start_money(start_money=200):

  opt = [200, 1000, 10000]
  print('\nHow high do you want the stakes to be?')
  not_valid = '\nYou must choose one of the valid options\n'

  while True:
    sleep(0.4)

    try:
      choice = int(input('Please, choose between option 1: {}, 2: {} or 3: {}\n'.format(opt[0], opt[1], opt[2])))
    except ValueError:
      print(not_valid) 
      continue

    if choice not in range(1, 4):
      print(not_valid)
      continue
    else:
      start_money = opt[choice-1]
      print('\nYou will be starting with {} dollars!'.format(start_money))
      break

  return start_money


# prompts user for a bet amount, returns the bet
def get_bet(self, player, max_bet):

  
  not_valid = """\nYou only have {} dollares available.\n
  Please input a valid amount\n""".format(max_bet)

  while True:
    try: 
      bet = int(input('\n{}, how much do you want to bet?\n'.format(player)))
    except ValueError:
      print(not_valid) 
      continue

    if bet > max_bet:
      print(not_valid)
      continue
    else:
      print('\n{} bet is {} dollars'.format(player, bet))
      break
  return bet


# asks if a player wants a new card 
def ask_hit(p_num):
  print('\nPlayer {}, would you like to Stand or Hit?'.format(p_num))

  while True:
    stand = input('Press S for Stand or H for Hit\n').upper()

    if stand == 'S':
      return False
    
    if stand == 'H':
      return True
    
    else:
      print('\nThat is not a valid option')
      continue
