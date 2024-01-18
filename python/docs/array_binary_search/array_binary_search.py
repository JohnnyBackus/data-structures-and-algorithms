test_list = [4, 8, 15, 16, 23, 42]
test_list_two = [-131, -82, 0, 27, 42, 68, 179]

# --------- first attempt: this approach will only work if the search key is at the middle position, because this function otherwise returns index position of half_list, not the original list  ---------

# def binary_search(list, search_key):
#     mid = len(list) // 2
#     if search_key not in list:
#         return -1
#     elif search_key == list[mid]:
#         return mid
#     elif search_key > list[mid]:
#         half_list = list[mid+1:]
#         return binary_search(half_list, search_key)
#     else:
#         half_list = list[:mid]
#         return binary_search(half_list, search_key)


# --------- second attempt: outside-in approach is the way to approach this so that I can reference indices of the original list  ---------

def binary_search(list, search_key):
    if search_key not in list:
        return -1
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid] == search_key:
            return mid
        elif list[mid] < search_key:
            start = mid + 1
        else:
            end = mid - 1

print(binary_search(test_list, 15))
print(binary_search(test_list_two, 42))
print(binary_search(test_list_two, -5))
