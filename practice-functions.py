"""There are 1,000 meters in one kilometer. The following function converts kilometers (km) to meters (m).
Complete the function to return the result of the conversion. 
NOTE: The following items occur outside of the function. Do not try to change the indentations on the 
associated code or you will receive an error.
Call the function to convert the trip distance from kilometers to meters..
Fill in the blank to print the result of the conversion.

"""

# 1) Complete the code to return the result of the conversion
def convert_distance(km):
	m = km * 1000  # exactly 1000 meters in 1 kilometer
	return m
# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above
my_trip_kilometers = 55

# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)
# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))


"""Pregunta 4
Complete the first line of the “print_seconds” function so that it accepts 
three parameters: hours, minutes, and seconds. Remember, to define a function, you use the def keyword 
followed by the function name and parentheses. The function parameters go inside the parentheses in the 
function definition, and they represent the values that will be given to the function when it is called. 
Also remember that the print function is a built-in Python function that outputs its arguments to the console. 
You call a function by using its name followed by parentheses, 
with the arguments for the function inside the parentheses."""

def print_seconds(hours, minutes, seconds):
   print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)
#output will print to the screen
