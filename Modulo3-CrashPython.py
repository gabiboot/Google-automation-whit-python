number = 1 # Initialize the variable
while (number < 8): # Complete the while loop condition
    print(number, end=" ")
    number +=1 # Increment the variable

# Should print 1 2 3 4 5 6 7 
    


    
for number in range(5):
    if number % 2 == 0:
        print("odd")
    else:
        print("even")


# Should print:
# odd
# even
# odd
# even
# odd
        



        
def digits(n):
    count = 0
    if n == 0:
        count += 1
    while n != 0:  # While there are still digits in n
        n //= 10   # Remove the last digit of n
        count += 1  # Increment the count for each removed digit
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1




def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high,low-1,-1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.





def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(0, max ): # Complete the for loop
        if x % divisor == 0:
            count +=1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9





def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for n in range(minimum, maximum+1): 

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        print(n)

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0