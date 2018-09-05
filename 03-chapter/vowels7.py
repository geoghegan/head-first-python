vowels = set('aeiou')
word = input("Provide a work to search for vowels: ")
found = vowels.intersection(set(word))

for vowel in found:
 print(vowel)
