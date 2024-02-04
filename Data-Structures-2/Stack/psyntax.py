# Check of valid parenthesis

def check_valid(s):
    stack = []
    map = {")":"(", "}":"{", "]":"["}

    for char in s:
        if char in map.values():
            stack.append(char)
        elif char in map.keys():
            popitem = stack.pop() if stack else None
            if map[char] != popitem:
                return False
        else:
            continue
    return not stack


input_string = "[{})"
print(check_valid(input_string))


