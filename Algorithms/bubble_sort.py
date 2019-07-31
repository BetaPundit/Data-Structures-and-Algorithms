def swap(num_list, first_index, second_index):
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def bubble_sort(num_list):
    total_no_of_passes = 0
    end_index = len(num_list)
    for index1 in range(0, end_index-1):
        swapped = False
        total_no_of_passes += 1
        for index2 in range(0, (end_index-index1-1)):
            if(num_list[index2] > num_list[index2+1]):
                swap(num_list, index2, index2+1)
                swapped = True
        if(swapped == False):
            break
    return total_no_of_passes


num_list = [8, 2, 19, 34, 23, 67, 91]
# num_list=[91,8,19,23,34,67,2]
print("Bubble Sort - No. of passes:", bubble_sort(num_list))
print("Sorted List: ", num_list)
