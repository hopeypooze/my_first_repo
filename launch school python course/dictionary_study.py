""" 
*******Accessing Keys:
**Get All Keys:


my_dict = {"apple": "a fruit", "book": "a collection of pages", "pen": "a writing tool"}

keys = my_dict.keys()
print(keys)  # Outputs: dict_keys(['apple', 'book', 'pen'])
.keys() returns a view object of all keys in the dictionary.



**Iterate Over Keys:


for key in my_dict.keys():
    print(key)

*****How to Work with Values:
**Access by Key:

**Use the key to get the associated value.


my_dict = {"apple": "a fruit", "book": "a collection of pages", "pen": "a writing tool"}
print(my_dict["apple"])  # Outputs: a fruit

**Iterate Over Values:

Use .values() to loop through all the values.

for value in my_dict.values():
    print(value)

**CHECKING FOR A KEY OR VALUE
in info → Checks for keys.
in info.values() → Checks for values.
in info.items() → Checks for key-value pairs as tuples.
 """
""" 
**Adding to a dictionary (flat):

#Add a new item, "pears", with a quantity of 12.
inventory['pears'] = (12)

#Update a value

inventory['apples'] = 20      # Reassignment of dict pair

**Remove from a dictonary

#Remove "bananas" from the dictionary.
if 'bananas' in inventory:
	del inventory['bananas']

***Adding to a Nested Dictionary:
python
Copy
Edit
grades = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 75, "english": 95},
}

# Add a new subject to Bob's grades
grades["Bob"]["science"] = 88

print(grades)


def word_lengths(my_dict):
	new_dict={}
	for key, value in my_dict.items():
		new_dict[key] = len(value)
	return new_dict

new_dict_var= word_lengths({"Mary":"girl", "Steve":"boy", "Hugo":"cat", "Lyra":"girl"})
print(new_dict_var)
 """






""" Exercise 1: Accessing Keys and Values
Given the dictionary:

info = {"name": "Alice", "age": 25, "city": "London"}
Print the value associated with the key "name".
Check if the key "age" exists in the dictionary.
Print all the keys and values using a loop. """

info = {"name": "Alice", "age": 25, "city": "London"}

# Print the value associated with the key "name"
print(info["name"])  # Outputs: Alice

# Test if a key doesn't exist in the dictionary
if "hat" not in info:  # 'not in' is the best way to check if a key is missing
    print("That's not in the dictionary")
else:
    print(info["hat"])  # This won't run since 'hat' is not in the dictionary

# Print all the keys and values using a loop
for key, value in info.items():
    print(key, value)


""" inventory = {"apples": 10, "bananas": 8, "oranges": 15}
Add a new item, "pears", with a quantity of 12.
Update the quantity of "apples" to 20.
Remove "bananas" from the dictionary. """

inventory = {"apples": 10, "bananas": 8, "oranges": 15}
print(inventory)

#Add a new item, "pears", with a quantity of 12.

inventory['pears'] = (12)
print(inventory)

#Update the quantity of "apples" to 20.

inventory['apples'] = 20      # Reassignment of dict pair
print(inventory)

#Remove "bananas" from the dictionary.
if 'bananas' in inventory:
	del inventory['bananas']
print(inventory)

""" Given this dictionary of students and their grades:

grades = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 75, "english": 95},
    "Charlie": {"math": 80, "english": 70}
}
Print Alice's grade in English.
Add a new subject, "science", with a grade of 88 for Bob.
Calculate and print the average math grade for all students. """

grades = {
    "Alice": {"math": 90, "english": 85},
    "Bob": {"math": 75, "english": 95},
    "Charlie": {"math": 80, "english": 70}
}

# Print Alice's grade in English
print(f"Alice's grade in English: {grades['Alice']['english']}")

#Add a new subject, "science", with a grade of 88 for Bob.
grades['Bob']['science'] = 88
print(grades)

#Calculate and print the average math grade for all students. 
grades_total=0
count_grades= []
for value in grades.values():
	count_grades.append(value['math'])
	grades_total += (value['math'])
	
count = len(count_grades)
my_average = grades_total / count
print(f'the average is {grades_total} divided by  {count} making {my_average}')