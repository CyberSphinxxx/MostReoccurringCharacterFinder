def most_occurring_character(string):
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
          
        else:
            char_frequency[char] = 1

    max_char = ''
    max_count = 0
    for char, count in char_frequency.items():
        if count > max_count:
            max_char = char
            max_count = count

    return max_char

input_string = input("Enter a string: ")
most_common = most_occurring_character(input_string)
print(f"The most occurring character is: {most_common}")
