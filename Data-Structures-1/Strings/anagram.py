# Anagram String

w1 = "listen"
w2 = "silent"

w1_dict = {c:w1.count(c) for c in w1}
w2_dict = {c:w2.count(c) for c in w2}

if w1_dict == w2_dict:
    print("Anagram")
else:
    print("Not anagram")