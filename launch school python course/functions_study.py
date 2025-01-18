""" Four-Step Process for Creating a Python Function
1. Define the Function

Choose a name for the function.
Add parameters as placeholders for inputs.

def function_name(parameter1, parameter2):

2. Describe the Function's Purpose

Write a comment explaining what the function does.

def function_name(parameter1, parameter2):
    # This function adds two numbers.
Add a return Statement

3. Determine what the function should output and include a return statement.

def function_name(parameter1, parameter2):
    # This function adds two numbers.
    result = parameter1 + parameter2
    return result

4. Call the Function

Provide arguments when calling the function.
Use print() to display the result if needed.

print(function_name(5, 10))  # Outputs: 15 """




#example of a function:

def square(num):  # Define function to calculate square  (num) is the PARAMETER.  the function performs its operation on num.
    return num * num  # Square of the number THIS LINE TELLS THE FUNCTION WHAT ITS JOB IS
print(f'the square is {square(3)}') # Substitutes 3 for the parameter num in the function square()


# example of a nested function
def square(num):  # Helper function to calculate square
    return num * num  # Square of the number 

def sum_of_squares(num1, num2):  # Main function
    return square(num1) + square(num2)  # Call square for each input and sum them

# Test the function
print(sum_of_squares(3, 4))   # 25 (3*3 + 4*4)
print(sum_of_squares(5, 12))  # 169 (5*5 + 12*12)


#practice function

#def times_two(num):  # Define function   (num) is the PARAMETER.  the function performs its operation on num.
 #   return num * 2  # STHIS LINE TELLS THE FUNCTION WHAT ITS JOB IS
#print(f'{num} doubled is {times_two(3)}') # Substitutes 3 for the parameter num in the function square()  WHY DOESNT THIS WORK - because num isn't a variable, it's privided as the argument to the function. how would we set this as a variable?

def times_two(num):  # Define function  (num) is the PARAMETER.  the function performs its operation on num.
    doubled = num * 2 #setting a variable which will be the output of the function
    return num, doubled, num * 2  # THIS IS THE OUTPUT OF THE FUNCTION 
print(f'the result is {times_two(3)}')

def cube_and_square(num):
    square = num ** 2
    cube = num ** 3
    return num, square, cube
argument, square, cube = (cube_and_square(3))
print(f'the cube of {argument} is {cube} and the square is {square}')

#Write a function called upper_and_lower that takes one argument, word. The function should:
#Return two values:
#The word converted to uppercase.
#The word converted to lowercase.  

def upper_and_lower(word):
		return word, word.upper(), word.lower()
argument, my_upper, my_lower = (upper_and_lower('Thursday'))
print(f'the word is {argument} uppercase: {my_upper} lowercase {my_lower}')

#Write a function called first_and_last that takes a string, text. The function should:return 2 values The first letter of the string.
#The last letter of the string.

def first_and_last(string):
      return string, string[0], string[-1]
#print('Friday'[0])
argument, first, last = (first_and_last('Friday'))
print(f'the string was {argument}. The first letter was {first} and the last letter was {last}')

#Write a function called reverse_and_length that takes a string, text. 

def reverse_and_length(string):
      return string, string[::-1], len(string)
argument, reversed, length = (reverse_and_length('Alphabet'))
print(f'reverse exercise: the string is {argument}, backwards it reads {reversed}. {argument} is {length} char long')

#Use multiple parameters for clarity and flexibility when dealing with distinct inputs. 
# Use tuple unpacking when handling grouped data that’s already structured as a single unit.

#working with multiple parameters:

#Exercise:
#Write a function called describe_person that takes three parameters:

#name (a string),
#age (an integer),
#hobby (a string).
#The function should:

#Return a sentence that describes the person using all three parameters.
#Then:

#Call the function with appropriate arguments.
#Print the returned sentence.

def describe_person(char1, char2, char3):
	return char1, char2, char3
name, age, hobby = (describe_person('Mary', 40, 'Painting'))


print(f'{name} is {age} years old and loves {hobby}')

#Write a function called area_and_perimeter that takes two parameters:
#length (a number),
#width (a number).

def area_and_perimeter(length, width): #define a function that takes two PARAMETERS which act as placeholders for the ARGUMENTS
      return length * width, 2*(length + width) #perform operations on the parameters and return 2 values, which we will set as area and perimeter variables in the next line
area, perimeter = (area_and_perimeter(4,2)) #Perform the function operation on the ARGUMENT. Set the result of the operation as 2 variables (2 because there are 2 values in the RETURN statement)
print(f'area: {area} perimeter: {perimeter}') #print the variables

#Write a function called circle_area_and_circumference that takes one parameter:
#radius (a number).
#The function should:
#Return two values:The area of the circle, The circumference of the circle

def circle_area_and_circumference(radius):
      return radius, (3.14 * (radius ** 2)), 2 * 3.14 * radius
radius, area, circumference = circle_area_and_circumference(4)
print(f'when the radius is {radius} the area is {area} and the circumference is {circumference}')

#DEFAULT PARAMETERS

#Write a function called greet that takes two parameters:

#name (a required string).
#greeting (an optional string that defaults to "Hello").
#The function should Return a personalised greeting using the name and greeting parameters.

def greet(name, greeting = 'Hello'):
      return greeting, name
greeting, name = greet('Hope') # when I have greet('Hope', 'hidehii') the greeting printed is hidehii.
print(f'{greeting}, {name}')


#KEYWORD ARGUMENTS

def function_name(parameter1, parameter2="default_value"):
    # Use the parameters in some way
    return f"Parameter1: {parameter1}, Parameter2: {parameter2}"

# Calling the function
print(function_name("value1"))              # Uses the default for parameter2
print(function_name("value1", "value2"))    # Overrides the default for parameter2


#By default, arguments are passed to functions as positional arguments unless you explicitly use keyword arguments. 
#If you used positional arguments, the order must match the function definition:
#Keyword arguments allow you to specify values for function parameters by explicitly naming them in the function call. This makes your code more self-explanatory and allows you to call arguments in any order.
#Write a function called create_profile that takes three parameters:

#name (a required string),
#age (a required integer),
#city (an optional string that defaults to "Unknown").
#The function should:
#Return a sentence that describes the profile in the format:
#Name: <name>, Age: <age>, City: <city>

def create_profile(name, age, city):
      return name, age, city
namev, agev, cityv = create_profile('Hope', age= 57, city= 'Gosford') # the keyword arguments must match the parameter names defined in the function.these arguments are specified by their keywords (parameter names), not just their position. variable names don't have to match keyword names.
print(f'Profile: name- {namev} age- {agev} city- {cityv}')

#Write a function called order_summary that takes four parameters:

#item (required string) — the name of the item being ordered.
#quantity (required integer) — the number of items being ordered.
#price_per_item (required float) — the price of a single item.
#discount (optional float, default value is 0.0) — a discount applied to the total price.
#The function should:

#Calculate the total cost using the formula:total cost=(quantity * price per item) - discount

#Return a summary of the order as a string.

def order_summary(item, quantity, price_per_item, discount):
       return ((quantity * price_per_item) - discount), item, quantity, price_per_item, discount
totalv, itemv, quantityv, price_per_itemv, discountv = order_summary(item="Laptop", quantity=2, price_per_item=799.99, discount=100.0)
     
print(f' Order Summary: {quantityv} {itemv} @ {price_per_itemv}, discount {discountv} total cost {totalv}')


#FUNCTIONS WITH CONDITIONAL LOGIC
#Exercise: Categorise a Number
#Write a function called categorise_number that takes one parameter, number. The function should:

#Return "positive" if the number is greater than 0.
#Return "negative" if the number is less than 0.
#Return "zero" if the number is exactly 0.

def categorise_number(number):
	if isinstance(number, int):
		if number > 0:
			return 'positive'
		elif number < 0:
			return 'negative'
		else:
			return 'zero'
		
	else:
		print("That's not a number")

result = categorise_number('a')
print(result) #put this outside the function, AFTER the result line.  

#FUNCTIONS WITH LOOPS
#Write a function called sum_of_squares that:

#Takes a single parameter, numbers, which is a list of integers.
#Calculates the sum of the squares of all the integers in the list.
#Returns the total.
numbers=()
def sum_of_squares(numbers):
	total = 0 #must initialise the list
	for num in numbers: #(loops through numbers)
		total += num ** 2 #total is acted upon every loop
	return total
print(sum_of_squares([1,2,3,4,5]))


#SUPER GENERIC FUNCTION BUILDING

def my_function(parameter1, parameter2): #define the function name and its parameters These are placeholders for the input(s) the function will use.
# concatenate p1 and p2 into an uppercase string
       result = str(parameter1.upper() + " " + parameter2.upper()) #result = is called an assignment statement. It assigns the result of an operation or expression to a variable.
       return result 												#makes the output of the operation above available to the function call below.
concatenated_string = my_function('hello', 'world') 				#calls the function and stuffs the 2 parameters into the spaces held by parameter1 and parameter2. sets the output as a variable.
print(concatenated_string)


#Write a function called double_numbers that:

#Takes a list of numbers as input.
#Doubles each number in the list.
#Returns a new list with the doubled values.

 
def double_numbers(num_list): #function called double_numbers that uses a parameter called num_list which will be supplied as an argument when we call the function
	new_list = [] #initialise an empty list to store the doubled numbers (outside the loop but inside the function)
	for num in num_list: #do this as many times as there are items in num_list
		new_list.append(num * 2) #append the doubled numbers to new_list 
	return new_list #makes the output of the operation above available to the function call below.

final_list = double_numbers([1,2,3,4,5]) 
print(final_list)


#Write a function called double_numbers that:

#Takes a list of numbers as input.
#Doubles EVEN NUMBERS in the list
#Returns a new list with the doubled values.

 
def double_numbers(num_list): #function called double_numbers that uses a parameter called num_list which will be supplied as an argument when we call the function
	new_list = [] #initialise an empty list to store the doubled numbers (outside the loop but inside the function)
	for num in num_list: #do this as many times as there are items in num_list
		if num % 2 == 0: #but only do it to even numbers
			new_list.append(num * 2) #append the doubled numbers to new_list 
	return new_list #makes the output of the operation above available to the function call below.

final_list = double_numbers([1,2,3,4,5]) 
print(final_list)

#Write a function called double_numbers that:
#Takes a list of numbers as input.
#according to user input
#Doubles ODD OR EVEN NUMBERS in the list
#Returns a new list with the doubled values.

choice = input("Should I double odd or even numbers? odd/even: ").lower()

if choice not in ['odd', 'even']:
    print('Invalid input. Please type "odd" or "even".')
else:
    print(f"You chose to double {choice} numbers.")

def odd_even_dbl(num_list): #function that uses a parameter called num_list which will be supplied as an argument when we call the function
#based on user input, adds odd or even numbers to new_list variable
	new_list = [] #initialize empty lists
	for num in num_list: #do this as many times as there are items in num_list
			if ((num % 2 == 0) and choice == 'even'): #only do it to even numbers
				new_list.append(num * 2) #append the doubled numbers to new_list
			elif ((num % 2 != 0) and choice == 'odd'):
				new_list.append(num * 2)
	return new_list #returns the list of odd or even numbers built during the for loop		

final_list = odd_even_dbl([1,2,3,4,5]) 
print(final_list)

# solo practice: write a function to add 2 numbers together
#with 2 parameters
def addition(num1, num2):
	result = num1 + num2
	return result, num1, num2

result, number1, number2 = addition(1,2) # Call the function and unpack the returned values

print(number1)

#solo practice a function containing a loop

def is_vowel(my_letters):
	vowel_list = []
	for let in my_letters:
		if let in ('aeiou'):
			vowel_list.append(let)
	return vowel_list

final_list = is_vowel('abc-123-xyz-789-iou')
print(final_list)

#FUNCTION USING A LIST

def count_evens(int_list):
	count=0
	for int in int_list:
		if int % 2 == 0:
			count += 1
	return count

counter = count_evens([1,2,3,4,5,6])

print(counter)

#FUNCTION USING A DICTIONARY

def word_lengths(my_dict):
	new_dict={}
	for key, value in my_dict.items():
		new_dict[key] = len(value)
	return new_dict

new_dict_var= word_lengths({"Mary":"girl", "Steve":"boy", "Hugo":"cat", "Lyra":"girl"})
print(new_dict_var)


