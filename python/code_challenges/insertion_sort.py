def insertion_sort(array):
    for i in range(1, len(array)):
        left_of_temp = i - 1
        temp = array[i]
        print(f"i: {i}\nleft_of_temp: {left_of_temp}\ntemp: {temp}\n")

        while left_of_temp >= 0 and temp < array[left_of_temp]:
            print(f"\ti: {i}\n\tleft_of_temp: {left_of_temp}\n\ttemp: {temp}\n")
            array[left_of_temp + 1] = array[left_of_temp]
            left_of_temp -= 1

            array[left_of_temp + 1] = temp

    return array


list = [8, 4, 23, 42, 16, 15]
print(insertion_sort(list))
