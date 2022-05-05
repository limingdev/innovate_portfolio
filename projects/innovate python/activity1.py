test_string = "We are CodeNation"
test_length = len(test_string)
print(test_length)

def length_checker(string):
    if len(string) % 2 == 0:
        return f"The length of the string: {string} is {len(string)} which is even."
    else:
        return f"The length of the string: {string} is {len(string)} which is odd."

string_list = ["hkfhakfhak", "How long is this string?", "How about this string?", "Is this one longer or shorter?", "Lorem ipsum"]
print(string_list)

for string in string_list:
    print(length_checker(string))

string_list.append("Here's a new string to add to the list")

print(string_list)