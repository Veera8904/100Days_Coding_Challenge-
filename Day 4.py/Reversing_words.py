#Reversing words in a string
def reverse_words(s):
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

s = "Hello i am a software developer"
print("Reversed words are:",reverse_words(s))

