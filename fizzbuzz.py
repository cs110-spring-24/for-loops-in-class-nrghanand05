#Print out all the numbers between 1 and 30
#If the number is a multiple of 3, instead of printing the number, print out “Fizz”
# If the number is a multiple of 5, instead of printing the number, print out “Buzz”
# If the number is a multiple of 15, instead of printing the number, print out “FizzBuzz”

for count in range (1,31):
    if count % 15 == 0: 
        print ("FizzBuzz")
    elif count % 3 == 0: 
        print ("Fizz")
    elif count % 5 == 0: 
        print ("Buzz")
    else:
        print (count)

