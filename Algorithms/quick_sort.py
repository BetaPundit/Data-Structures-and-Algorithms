def swap(num_list, first_index, second_index):
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def quick_sort(num_list, low, high):
    if(low >= high):
        return
    split_point = partition(num_list, low, high)
    quick_sort(num_list, low, split_point-1)
    quick_sort(num_list, split_point+1, high)


def partition(num_list, low, high):
    pivot = num_list[low]
    i = low+1
    j = high
    done = False
    while not done:
        while (i <= j and num_list[i] <= pivot):
            i = i+1
        while(num_list[j] >= pivot and j >= i):
            j = j-1
        if(j < i):
            done = True
        else:
            swap(num_list, i, j)
    swap(num_list, low, j)
    return j


num_list = [3, 1, 0, 4, 2]
print("Before sorting;", num_list)
l = len(num_list)
quick_sort(num_list, 0, l-1)
print("After sorting:", num_list)
