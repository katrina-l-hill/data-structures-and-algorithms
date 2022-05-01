def insertShiftArray(item_list, insert_value):
    middle = find_middle_index(item_list)
    count = get_item_count(item_list)
    output = []
    index = 0
    while index < count:
        if index == middle:
            # insert new value, then original value for this index
            output += [insert_value]
            output += [item_list[index]]
        else:
            output += [item_list[index]]
        index += 1
    return output


def find_middle_index(item_list):
    # get the item in the list, and place it in the middle
    count = get_item_count(item_list)
    if count % 2 == 0:
        return (int)(get_item_count(item_list) / 2)
    else:
        return (int)(get_item_count(item_list) / 2) + 1


def get_item_count(item_list):
    count = 0
    for i in item_list:
        count += 1
    return count


list1 = [2, 4, 6, -8]
list2 = [42, 8, 15, 23, 42]

print(insertShiftArray(list1, 5))
print(insertShiftArray(list2, 16))
