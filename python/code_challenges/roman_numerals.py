# Pseudo code

# def roman_to_arabic(roman):
#     total = 0

#     for i in range(len(roman) - 1):
#         left_char = roman[i]
#         right_char = roman[i + 1]
#         left_value = convert_character(left_char)
#         right_value = convert_character(right_char)

#         if left_value < right_value:
#             left_value = -left_value

#         total += left_value

#     if roman:
#         total += convert_character(roman[-1])

#     return roman


# def convert_character(roman_char):
#     conversion_map = {
#         "M": 1000,
#         "D": 500,
#         "C": 100,
#         "L": 50,
#         "X": 10,
#         "V": 5,
#         "I": 1,
#     }

# return conversion_map.get(roman_char, 0)


def roman_to_arabic(input):
    total = 0
    roman_numeral_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
    }
    input_len = len(input)
    print(f"input_len: {input_len}")
    for i in range(input_len):
        if i < input_len - 1:
            # normal case
            left_char = input[i]
            right_char = input[i + 1]
            left_val = roman_numeral_dict[left_char]
            right_val = roman_numeral_dict[right_char]
            if left_val < right_val:
                left_val = left_val * -1
            total += left_val
        else:
            # end of input case
            char = input[i]
            val = roman_numeral_dict[char]
            total += val
        print(f"i: {i}, total: {total}")

    return total


print(roman_to_arabic("MCMLXXXIV"))
print(roman_to_arabic("CXLII"))
