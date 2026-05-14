print("Hello, World!")
name = input("Enter Your Name: ")
print("Welcome, " + name + "!")

#input an array from user
arr = input("Enter an array of elements: ")
arr = arr.split()
arr = [int(x) for x in arr]
print("You entered: ", arr)

print(type(arr))
a = 2
#data type

print(type(a))

good = True
print(type(good))


# unsorted list
list = [5, 2, 9, 1, 5, 6]
print("Unsorted list:", list)
print(type(list))
print(sorted(list))
print(sorted(arr))

# tupple 
tup = (1, 2, 3, 4, 5)
print("Tupple: ", tup)

# set 
set = {1, 2, 3, 4,4,5, 5}
print("Set: ", set)
set.pop()
print("Set after popping an element: ", set)
set.add(6)
print("Set after adding an element: ", set)
set.remove(2)
print("Set after removing an element: ", set)

# dict using for mapping

person = {
    "name": "Jamiul",
    "age": 25,
    "city": "Dhaka"
}
print("Person: ", person)

print("Name: ", person["name"])
print("Age: ", person["age"])
print("City: ", person["city"])

nums = [5, 12, 17, 20, 3]
numsEven = []

# find greater than 10 and even numbers
for num in nums:
    if num > 10 and num % 2 == 0:
        numsEven.append(num)
print("Greater than 10 and even numbers: ", numsEven)

