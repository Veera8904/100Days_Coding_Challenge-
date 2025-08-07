#Duplicate letters in a string
def duplicate_letters(s):
    count = {}
    duplicates = []

    for char in s.lower():
        if char == " ":
            continue
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for char, freq in count.items():
        if freq > 1:
            duplicates.append(char)

    return "".join(duplicates) 

s = "veerendra kumar"
print("Duplicate letters are:", duplicate_letters(s))
