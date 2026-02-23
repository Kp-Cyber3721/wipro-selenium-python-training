#dictionary item - key value
#similar to list and tuples
#for integers, tuples and strings - keys Must be immutables
#list cannot be used in the key for the dict as it is mutable in nature
country = {
    "India":"Delhi",
    "Canada":"Ottawa",
    "England":"London",
}
print(country)
#access the values with keys
print(country["Canada"])

#add elements
country["Italy"]="Rome"
print(country)
#remove elements
del country["India"]
print(country)

#claer
#country.clear()
#print(country)

#iterate among the dict
for coun in country:
    print(coun)
#for integers - keys Must be immutables
#list as key
#my_dict={1:"hello",[1,2]:"There"}
#print(my_dict)

#integer as a key
my_dict={1:"one",2:"Two",3:"Three"}
print(my_dict)

my_dict={1:"Four",2:"Two",3:"Three"}
print(my_dict)

#for tuples- keys Must be immutables


#tuples as a key
my_dict={(1,2):"one two",3:"three"}
my_dict={(1,2):"one two",3:"three",3:"four"}
print(my_dict)

#pop - removes the items with spec key
country.pop("Canada")
print(country)

#update() -adds or changes the dict
country.update({"USA": "DC"})
print(country)

#keys
print(country.keys())

#popitem() return the last inserted item
item = country.popitem()
print(item)
print(country)

#copy returns the copy of the dict
newcountry = country.copy()
print(newcountry)

#dict inside the list
employees = [
    {"id":1,"name":"Harsha","role":"QA"},
    {"id": 2, "name": "Anil", "role": "Dav"},
    {"id": 3, "name": "Ravi", "role": "Manager"}

]
print(employees[0])
print(employees[0]["name"])

for emp in employees:
    print(emp["name"],emp["role"])
#add the data
employees.append({"id":4,"name": "Sita","role":"Tester"})
print(employees)

#for deleting
employees.pop(0)
print(employees)

#search a item in the list
for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)



