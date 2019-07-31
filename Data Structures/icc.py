# DSA-Assgn-17


def find_matches(country_name):
    new_list = []
    for match in match_list:
        if country_name in match:
            new_list.append(match)
    return new_list


def max_wins():
    new_dict = {}
    temp_list = []
    tournament_list = []

    for match in match_list:
        match_details = match.split(':')
        temp_list.append(match_details)

    # get distinct tournaments
    for match in temp_list:
        if match[1] not in tournament_list:
            tournament_list.append(match[1])

    for j in range(len(tournament_list)):
        country_list = []
        max = 0
        for i in range(len(temp_list)):
            if tournament_list[j] in temp_list[i]:
                if max < int(temp_list[i][3]):
                    max = int(temp_list[i][3])

        for i in range(len(temp_list)):
            if tournament_list[j] == temp_list[i][1] and max == int(temp_list[i][3]):
                country_list.append(temp_list[i][0])

        new_dict[tournament_list[j]] = country_list

    return new_dict


def find_winner(country1, country2):
    count1 = 0
    count2 = 0
    for match in match_list:
        if country1 in match:
            count1 += int(match[-1])
        elif country2 in match:
            count2 += int(match[-1])
    if count1 > count2:
        return country1
    elif count2 > count1:
        return country2
    else:
        return 'Tie'


# Consider match_list to be a global variable
match_list = ["AUS:CHAM:5:2", "AUS:WOR:2:1", "ENG:WOR:2:0", "IND:T20:5:3",
              "IND:WOR:2:1", "PAK:WOR:2:0", "PAK:T20:5:1", "SA:WOR:2:0", "SA:CHAM:5:1", "SA:T20:5:0"]

# Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)

print(max_wins())

print(find_winner("AUS", "IND"))


# Initial Code:
'''
def find_matches(country_name):
    pass

def max_wins():
    pass

def find_winner(country1, country2):
    pass

# Consider match_list to be a global variable
match_list = ["AUS:CHAM:5:2", "AUS:WOR:2:1", "ENG:WOR:2:0", "IND:T20:5:3",
              "IND:WOR:2:1", "PAK:WOR:2:0", "PAK:T20:5:1", "SA:WOR:2:0", "SA:CHAM:5:1", "SA:T20:5:0"]

# Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)

print(max_wins())

print(find_winner("AUS", "IND"))

'''
