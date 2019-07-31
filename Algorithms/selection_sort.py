def swap(num_list, first_index, second_index):
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def find_next_min(num_list, start_index):
    smallest_index = start_index
    for i in range(start_index, len(num_list)-1):
        if num_list[smallest_index] > num_list[i+1]:
            smallest_index = i+1
    return smallest_index


def selection_sort(num_list):
    total_no_of_passes = 0
    for i in range(len(num_list)):
        total_no_of_passes += 1
        next_index = find_next_min(num_list, i)
        if next_index != i:
            swap(num_list, i, next_index)
    return total_no_of_passes-1


num_list = [8, 2, 19, 34, 23, 67, 91]
# num_list=[91,8,19,23,34,67,2]
print("Selection Sort - No. of passes:", selection_sort(num_list))
print("Sorted List: ", num_list)
