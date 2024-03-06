"""The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 
Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". This function should:
accept a string through the parameters of the function;
separate the address string into new strings: house_number and street_name; 
return the variables in the string format: "House number X on a street named Y". """

def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split(" ")
    
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.strip()

    # Use the formatted variables to create the final string.
    formatted_address = f"House number {house_number} on a street named {street_name}"

 
    # Use a string method to return the required formatted string.
    return formatted_address


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"


"""Fill in the blank to complete the “highlight_word” function. 
This function should change the given “word” to its upper-case version in a given “sentence”. 
Complete the string method needed in this function so that a function 
call like "highlight_word("Have a nice day", "nice")" will return the output "Have a NICE day"."""

def highlight_word(sentence, word):
    # Complete the return statement using a string method.

    if word in sentence:
        
     new_sentence = sentence.replace(word, word.upper())


    return new_sentence


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"

"""Consider the following scenario about using Python lists: 
Employees at a company shared  the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the shortest distance. 
Complete the function to sort the “distances” list. This function should:
sort the given “distances” list, passed through the function’s parameters; ; 
reverse the sort order so that it goes from the longest to the shortest distance;
return the modified “distances” list."""

def sort_distance(distances):
    order = distances.sort(reverse=True) # Sort the list
    # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

"""Fill in the blank to complete the “squares” function. 
This function should use a list comprehension to create a list of squared numbers (using either the expression n*n or n**2). 
The function receives two variables and should return the list of squares that occur between the “start” and “end” 
variables inclusively (meaning the range should include both the “start” and “end” values). 
Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”."""

def squares(start, end):
    return [ n**2 for n in range(start,end+1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Fill in the blanks to complete the “car_listing” function. 
This function accepts a “car_prices” dictionary. 
t should iterate through the keys (car models) and values (car prices) in that dictionary. 
For each item pair, the function should format a string 
so that a dictionary entry like ““Kia Soul“:19000” will print "A Kia Soul costs 19000 dollars". 
Each new string should appear on its own line."""


def car_listing(car_prices):
  result = ""
  # Complete the for loop to iterate through the key and value items 
  # in the dictionary.
  for model, price in car_prices.items():
    result += "A {} costs {} dollars\n".format(model,price) # Use a string method to format the required string. 
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# Should print:
# A Kia Soul costs 19000 dollars
# A Lamborghini Diablo costs 55000 dollars
# A Ford Fiesta costs 13000 dollars
# A Toyota Prius costs 24000 dollars

"""Pregunta 6
Consider the following scenario about using Python dictionaries: 
tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one collected responses into dictionaries, with names of their friends and how many guests each friend was bringing. Each dictionary is a partial guest list, but Rick's guest list has more current information about the number of guests. 
Complete the function to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rick's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary. This function should:
accept two dictionaries through the function’s parameters;
combine both dictionaries into one, with each key listed only once;
the values from the “guests1” dictionary taking precedence, if a key is included in both dictionaries;
then print the new dictionary of combined items."""

def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}


"""Consider the following scenario about using Python dictionaries:
A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100.  Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it for Term 2. The student name keys in the dictionary should stay the same, but the grade values should be reset to 0.
Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 
accept a dictionary “old_gradebook” variable through the function’s parameters;
make a copy of the “old_gradebook” dictionary;
iterate over each key and value pair in the new dictionary;
replace the value for each key with the number 0;
return the new dictionary."""

def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook. 
  for name, value in new_gradebook.items():
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[name] =0
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}

