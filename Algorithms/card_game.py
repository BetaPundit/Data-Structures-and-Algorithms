#DSA-Tryout
import random

def generate_cards_per_type(card_type):
    if card_type == 'C':
        val = 100
    elif card_type == 'D':
        val = 200
    elif card_type == 'H':
        val = 300
    elif card_type == 'S':
        val = 400
    card_list = []
    for i in range(2, 15):
        card = {'name': None, 'value': None}
        if i > 10:
            if i == 11:
                card['name'] = card_type+'J'
                card['value'] = i + val
                card_list.append(card)
            elif i == 12:
                card['name'] = card_type+'Q'
                card['value'] = i + val
                card_list.append(card)
            elif i == 13:
                card['name'] = card_type+'K'
                card['value'] = i + val
                card_list.append(card)
            else:
                card['name'] = card_type+'A'
                card['value'] = i + val
                card_list.append(card)
        else:
            card['name'] = card_type+str(i)
            card['value'] = i + val
            card_list.append(card)
    return card_list

def generate_card_deck():
    deck = []
    deck += generate_cards_per_type('C')
    deck += generate_cards_per_type('D')
    deck += generate_cards_per_type('H')
    deck += generate_cards_per_type('S')
    return deck

def shuffle_card_deck(cards_list):
    last = len(cards_list)-1
    mid = len(cards_list)//2
    left_list = cards_list[:mid]
    right_list = cards_list[mid:]
    
    for i in range(mid):
        random_num = random.randrange(0,mid,3)
        temp = left_list[i]
        left_list[i] = right_list[random_num]
        right_list[random_num] = temp
    return left_list + right_list

def sort_cards_of_each_player(card_list):
    card_list.sort(key = lambda x: x['value'])
    return card_list


def allocate_cards_to_players(cards_list):
    player_dict = {'player1':[], 'player2':[], 'player3':[], 'player4':[]}
    players = ['player1', 'player2', 'player3', 'player4']

    for i in range(len(cards_list)):
        player_dict[players[i%4]].append(cards_list[i])

    return player_dict

def prepare_cards():
    start_player = ''
    deck = generate_card_deck()
    shuffled_deck = shuffle_card_deck(deck)
    print(shuffled_deck)
    player_decks = allocate_cards_to_players(shuffled_deck)
    # print(player_decks)

    for player in player_decks:
        sorted_deck = sort_cards_of_each_player(player_decks[player])
        
        for card in sorted_deck:
            # print(card)
            if 'CA' == card['name']:
                print('True')
                start_player = player

    # print(player_decks)
    return start_player


first_player=prepare_cards()
print("The first player is:",first_player)