my_string = "My name is Sidharth"
# Replace characters in a String
def replace_char(string, char, pos):
    new_str = ""
    for i in range(len(string)):
        if i == pos:
            new_str+=char
        else:
            new_str+=string[i]
    return new_str

replaced_str = replace_char(my_string, "B", 8)
print(replaced_str)