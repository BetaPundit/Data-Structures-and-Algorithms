def make_change(denomination_list, amount):
    result_list = []
    if amount in denomination_list:
        return 1
    
    while(amount > 0):
        if len(denomination_list) == 0:
            return -1
        max_val = max(denomination_list)
        if amount >= max_val:
            amount -= max_val
            result_list.append(max_val)
            if amount == 0:
                print(result_list)
                return len(result_list)
        else:
            denomination_list.remove(max_val)


#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
result = make_change(denomination_list, amount)
print(result)