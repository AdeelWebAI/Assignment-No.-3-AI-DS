# Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.

# Access the value of the key grade in the student dictionary.

# Add a new key city to the student dictionary and set its value to "New York".

# Update the value of the age key in the student dictionary to 20.

# Remove the key city from the student dictionary.


# students = {
#     "name": "bahawal",
#     "age": 20 ,
#     "grade": "A+",
# }
# students["city"] = "New York"
# students["age"] = 29
# del students["city"]
# print(students)




# Iterating through Dictionaries

# Iterate through the dictionary student and print all keys.

# Iterate through the dictionary student and print all values.

# Iterate through the dictionary student and print all key-value pairs in the format key: value.

# Check if the key grade exists in the student dictionary and print True or False.

# Count the total number of keys in the student dictionary.


# students = {
#     "name": "bahawal",
#     "age": 20 ,
#     "grade": "A+",
# }

# for value  in students.values():
#     print(value)

# for key , value in students.items():
#     print(key , " : ",  value)

# if "grade" in students:
#     print(True)
# else:
#     (False)

# print(students.__len__())

# Advanced Dictionary Usage
# Merge the following two dictionaries and print the result:

# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  


# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)
# another method to add two dictionaries is with unpacking operator that is ** (double star or double multiple sign)

# total = {**dict1, **dict2}
# print(total)

# Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].
# dict = {"name": "Alice",
#         "age": 25,
#         "city": "Paris",
#         }

# dict = {'z': 1, 'a': 2, 'c': 3}

# sorted_dictionary = sorted(dict.keys())
# print(sorted_dictionary)

# Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.

# dict = {'z': 1, 'a': 2, 'c': 3}
# reversed_dictionary = {value: key for key, value in dict.items()}
# print(reversed_dictionary)

# Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.

# dict = {'z': 1, 'a': 2, 'c': 3}
# ass_dict = sorted(dict.keys())
# print(ass_dict)

# Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).

# dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  

# def check_identical(dict1, dict2):
#     return dict1 == dict2
# print(check_identical(dict1, dict2))


# Nested Dictionaries

# Create a nested dictionary to represent the following data:
# Person:  
#   Name: John  
#   Age: 30  
#   Address:  
#     Street: 123 Elm St  
#     City: Boston  
   
person = {
    "Name": "John",
    "Age": 30,
    "Address": {
        "Street": "123 Elm St",
        "City": "Boston",
    },
}
# Access the value of the City key in the nested dictionary from the previous question.

# print(access_value)
# access_value = person["Address"]["City"]

# Add a new key Phone to the nested dictionary with the value "123-456-7890".
person["Address"]["Phone"] = "123-456-7890"

# Delete the Address key from the nested dictionary.

del person["Address"]

# Iterate through all the keys in the outermost level of the nested dictionary and print them.

for key in person.keys():
    print(key)
    
    
# print(person)
