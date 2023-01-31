from art import logo
import os
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player, dealer):
    if player > 21 and dealer > 21:
        return "You went over. You lose"
    if player == dealer:
                return "Draw"
    elif dealer == 0:
            return "Lose, opponent has Blackjack"
    elif player == 0:
        return "Win with a Blackjack"
    elif player > 21:
        return "You went over. You lose"
    elif dealer > 21:
        return "Opponent went over. You win"
    else:
        return "You lose"

def play_game():
    
    print(logo)
    
    player_cards = []
    dealer_cards = []
    is_game_over = False
    
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())
    
    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
    
        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {dealer_cards[0]}")
    
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            isContinue = input("Type 'y' to get another card, type 'n' to pass: ")
        
            if isContinue == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
            else:
                is_game_over = True
            
            while dealer_score != 0 and dealer_score < 17:    
                dealer_cards.append(deal_card())
                dealer_score = calculate_score(dealer_cards)
                    
        print(f"   Your final hand: {player_cards}, final score: {player_score}")
        print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()