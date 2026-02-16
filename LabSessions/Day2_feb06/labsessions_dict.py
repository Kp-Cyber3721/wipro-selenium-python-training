#Create a dictionary with student roll number as key and name as value. Print the dictionary.
students = {
    201: "Karan",
    202: "Neha",
    203: "Suman"
}
print(students)
#Access the value of a key that exists and one that does not exist
print(students[202])
print(students.get(105))

#Update the value of an existing key in a dictionary.
students[203] = "Rohit"
print(students)
#Delete a key from a dictionary using:
#del
#pop()
del students[201]
print(students)
students.pop(202)
print(students)
#Find the number of key–value pairs in a dictionary.
print(len(students))
#Print only:
#keys
#values
#key–value pairs
print(students.keys())
print(students.values())
print(students.items())

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
new_dict = dict1.copy()
new_dict.update(dict2)
print(new_dict)


