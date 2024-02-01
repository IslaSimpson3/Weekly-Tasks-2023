#words into an array

words = ["hello", "world", "plant", "people"]
combinations = []


for i in words:
    for j in words:
        if i != j:              # <-- making sure the same word doesnt appear twice 
            combine = words[i] + " " + words[j]
            combinations.append(combine)

for combine in combinations:
    print(combine)
