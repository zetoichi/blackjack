from time import sleep

import prompts # functions that request input from users, checking validity
import cards # imports Cards class, which contains methods for simulating a deck
import bets # imports Bets class, which contains methods for managing and logging bets


# all sequences created have index 0 == None, for correlation with player number
# Dealer is always last

# defines basic variables
def setup_game(start_money):
  p_list = prompts.get_players() # creates list of players
  b = bets.Bets(p_list, start_money) # instance of Bets class
  c = cards.Cards(len(p_list)) # instance of Cards class
  print('\nThe table is set!\n')

  return b, c

# general game flow
def play_game():

  print('\nGreat!')
  start_money = prompts.get_start_money() # defines bankroll
  first_hand = True
  
  while True:

    if first_hand:
      sleep(0.4)
      b, c = setup_game(start_money)
       
    # gets bet from players, prints it, stores it
    sleep(0.4)
    b.place_your_bets()

    # gets first hand from deal, prints it, stores it
    sleep(0.4)
    c.get_all_hands(b.bets_log)

    # gets players final hand by hit or stand, checks if PLAYER LOST
    if b.check_statuses():
      sleep(0.4)
      c.hit_or_stand(b.bets_log)
    
      # gets dealer final hand by hit or stand. check if HOUSE BUST 
      if b.check_statuses(): 
        sleep(0.4)
        c.dealer_turn(b.bets_log)

        # checks remainig players' hand to see who won
        if b.check_statuses(): 
          sleep(0.4)
          c.check_win(b.bets_log)

    # asks for a new hand, quits if no
    sleep(0.4)
    print('\nDo you want to play another hand?\n')
    if not prompts.game_on():
      print('\nThanks for playing... See you next time!\n')
      break

    # updates Playing status in log, shuffles and deals
    else:
      b.update_status()
      c.shuffle_n_deal()
      first_hand = False  # avoids re-setting bankroll
      continue
    

print('\nWelcome to the Blackjack table')
sleep(0.4)
print('\nDo you want to start playing?')

if prompts.game_on():
  sleep(0.4)
  play_game()