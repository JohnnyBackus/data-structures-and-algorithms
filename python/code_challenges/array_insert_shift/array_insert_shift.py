test_array_one = [1, 2, 3, 4]
test_array_two = [1, 2, 3, 4, 5]

def insert_shift_array(arr, val):
    first_half = arr[:len(arr)//2]
    second_half = arr[len(arr)//2:]
    first_half.append(val)
    new_arr = first_half + second_half
    return new_arr
