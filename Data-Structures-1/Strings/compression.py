import re

string = "aabcccccaaa"
compressed = ""

def extract(input_string):
    pattern = re.compile(r'(\w)\1*')
    return [match.group() for match in pattern.finditer(input_string)]

result_arr = extract(string)
for strs in result_arr:
    compressed+=strs[0]
    compressed+=str(strs.count(strs[0]))

print(compressed)
