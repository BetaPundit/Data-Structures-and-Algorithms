def arrange_tickets(tickets_list):
    temp_list = []
    for i in range(1, 21):
        if 'T'+str(i) in tickets_list:
            temp_list.append('T'+str(i))
        else:
            temp_list.append('V')
    print(temp_list)
    g1 = temp_list[:10]
    g2 = temp_list[10:]

    for i in range(len(g1)):
        if g1[i] == 'V':
            for ticket2 in g2:
                if ticket2 != 'V':
                    g1[i] = ticket2
                    g2.remove(ticket2)
                    break
    return g1


tickets_list = ['T5', 'T7', 'T1', 'T2', 'T8',
                'T15', 'T17', 'T19', 'T6', 'T12', 'T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result = arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
