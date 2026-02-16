#sets do not allow duplicate eliments it contains only unique data
#unordered collection
#create a student_id set integer type
stu_id = {112, 113, 114, 115, 115, 116 , 8 , 10, 45}
print(stu_id)

#create a string type set
letters= {'a', 'b', 'c', 'd', 'e'}
print(letters)

#create a mixed set
mixed_set = {"Hello", 1,-7,8.9}
print(mixed_set)

#create an empty set
empty_set = set()

#adding set methods
stu_id.add(200)
print(stu_id)

stu_id.update([300, 400])
print(stu_id)

stu_id.remove(10)
print(stu_id)

stu_id.discard(999)
print(stu_id)

x = stu_id.pop()
print(x)
print(stu_id)

copy_set = stu_id.copy()
print(copy_set)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))


print(A.intersection(B))


print(A.difference(B))


print(A.symmetric_difference(B))


A.intersection_update(B)
print(A)

B.difference_update({4, 5})
print(B)

print({1, 2}.issubset({1, 2, 3}))
print({1, 2, 3}.issuperset({1, 2}))
print({1, 2}.isdisjoint({3, 4}))

letters.clear()
print(letters)

largest = max(A)
print(largest)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_number = []
for num in numbers:
    if num % 2 != 0:
        odd_number.append(num)
print(odd_number)

result = 1
for num in numbers:
    result = result * num

print(result)
