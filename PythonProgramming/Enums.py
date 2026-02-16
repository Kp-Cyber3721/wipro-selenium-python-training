#enumerate with list
fruits = ["orange","cherry", "kiwi"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

#enumerate with start value changed from 0 to 1
for index,fruit in enumerate(fruits, start=1):
    print(index,fruit)

#enumerate with strings
word="python"
for i,ch in enumerate(word,start=2):
    print(i,ch)

#enumerate with tuples
fruits = ("orange","cherry", "kiwi")
for index,fruit in enumerate(fruits):
    print(index,fruit)

#real time scenario
test_cases= ["Login","signup","Checkout"]
for case_no, test in enumerate(test_cases, start=1):
    print(f"Executing Testcase {case_no}:{test}")

a=['God','is','Great']
b=enumerate(a)
next_val =next(b)
print(next_val)
print(next_val)

characters = ["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
    "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
    "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]
character_map = {character:[] for character in set(characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)