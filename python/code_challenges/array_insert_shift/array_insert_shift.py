test_list_one = [1, 2, 3, 4]
test_list_two = [1, 2, 3, 4, 5]

def insert_shift_array(list, val):
    first_half = []
    second_half = []
    for i in range(len(list)):
        if i <= len(list)//2:
            first_half.append(list[i])
        else:
            second_half.append(list[i])
    first_half.append(val)
    new_list = first_half + second_half
    return new_list

print(insert_shift_array(test_list_one, 10))
print(insert_shift_array(test_list_two, 10))
