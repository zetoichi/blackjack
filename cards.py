import random as r
import bets

from time import sleep
from prompts import ask_hit

class Cards:

  # creates a list of tuples as a deck of cards and shuffles it
  def __init__(self, n_players=2):
    
    self.n_players = n_players
    self.new_deck = [
      ('A',11), ('2',2), ('3',3), ('4',4),
      ('5',5), ('6',6), ('7',7), ('8',8),
      ('9',9), ('Jack',10), ('Queen',10), ('King',10),
    ] * 4
    self.deck = self.deck_shuffle()
    self.deal = self.get_deal()


  # shuffles deck
  def deck_shuffle(self):
    
    deck = self.new_deck
    r.shuffle(deck)
    return deck

  
  # gets tuples from the deck for each player
  def get_deal(self):
    
    print('\nDealing cards...')
    deal = [None] + [[self.remove_card()] for i in range(self.n_players)]
    
    for p in deal[1:]:
      p.append(self.remove_card())
    
    sleep(0.4)
    return deal


  # shuffles and deals
  def shuffle_n_deal(self):
    
    self.deck = self.deck_shuffle()
    print('Shuffling!')
    sleep(0.4)
    self.deal = self.get_deal()
    
  
  # takes a card from the deck
  def remove_card(self):
    
    card = self.deck.pop()
    return card
  
  
  # gets player hands from deal, prints them, stores them in log
  def get_all_hands(self, bets_log):
    
    for i in range(1, len(self.deal)-1):
      hand = self.deal[i]
      name = bets_log[i]['Name']
      print('\n{} has a {} and a {}'.format(name, hand[0][0], hand[1][0]))
      
      if hand[0][0] == hand[1][0] == 11:
        hand[0] = ('A', 1)
      
      if self.check_blackjack(hand):
        bets_log[i]['Current Bet'] /= 2
        self.win_hand(i, bets_log)
      bets_log[i]['Current Hand'] = hand
    
    d_hand = self.deal[-1]
    print('\nThe Dealer\'s first card is a {}\n'.format(d_hand[0][0]))
    bets_log[-1]['Current Hand'] = d_hand
  
  
  # returns True if a hand totals 21
  def check_blackjack(self, hand):
    return self.get_hand_value(hand) == 21

  
  # changes the Ace value from 11 to 1
  # called automatically when a player holding an ace goes above 21
  def replace_ace(self, hand):
    ace, ace_1 = ('A', 11), ('A', 1)

    for i in range(len(hand)):
      if hand[i] == ace:
        hand[i] = ace_1
    
    return hand
  
  
  # takes a new card from the deck, returns its value
  def hit_or_stand(self, bets_log):
    
    for i in range(1, len(bets_log)-1):
      hand = bets_log[i]['Current Hand']
      hand_value = self.get_hand_value(hand)
      
      while ask_hit(i):
        new_card = self.remove_card()
        print('\nPlayer {} got a {}'.format(i, new_card[0]))
        hand_value += new_card[1]
        print('Player {} hand total is {}'.format(i, hand_value))
        
        if hand_value > 21:
          hand = self.replace_ace(hand)
          if hand_value > 21:                    # PLAYER LOST
            self.lose_hand(i, bets_log)
            break
          else:              
            continue
        
        else:
          hand.append(new_card)
          continue

  
  # takes a card tuple, returns its value
  def get_hand_value(self, hand):
    
    value = 0
    for card in hand:
      value += card[1]
    return value
  

  # dealer hits or stands depending on hand value, 
  def dealer_turn(self, bets_log):
    
    d_hand = bets_log[-1]['Current Hand']
    print('\nDealer\'s second card: {}'.format(d_hand[1][0]))
    d_hand_value = self.get_hand_value(d_hand)
    print('Dealer hand total is {}'.format(d_hand_value))
    while d_hand_value < 17:
      print('\nDealer hits\n')
      new_card = self.remove_card()
      print('\nDealer got a {}\n'.format(new_card[0]))
      d_hand_value += new_card[1]
      
      if d_hand_value > 21:         
        d_hand = self.replace_ace(d_hand)
        if d_hand_value > 21:                     # HOUSE BUST
          self.house_bust(bets_log)
          break
        else:
          d_hand.append(d_hand)
          continue
  

  # all active players win when house loses
  def house_bust(self, bets_log):

    for i in range(1, len(bets_log)-1):
      if bets_log[i]['Playing'] == True:
        self.win_hand(i, bets_log)


  # check remainig players to see who won
  def check_win(self, bets_log):
    d_hand_value = self.get_hand_value(bets_log[-1]['Current Hand'])

    for i in range(1, len(bets_log)-1):
      if bets_log[i]['Playing'] == True:
        hand_value = self.get_hand_value(bets_log[i]['Current Hand'])
        if hand_value > d_hand_value:
          self.win_hand(i, bets_log)
        else:
          self.lose_hand(i, bets_log)
  
  
  # announces win, updates a player's bankroll
  def win_hand(self, p_num, bets_log):

    print('\nPlayer {} won!'.format(p_num))
    bets_log[p_num]['Bankroll'] += bets_log[p_num]['Current Bet']
    bets_log[p_num]['Playing'] = False
    print('Player {} now has {} to gamble'.format(p_num, bets_log[p_num]['Bankroll']))

  
  # announces loss, updates a player's bankroll
  def lose_hand(self, p_num, bets_log):

    print('\nPlayer {} lost!'.format(p_num))
    bets_log[p_num]['Bankroll'] -= bets_log[p_num]['Current Bet']
    bets_log[p_num]['Playing'] = False
    print('Player {}\'s bankroll is down to {} dollars'.format(p_num, bets_log[p_num]['Bankroll']))

  

