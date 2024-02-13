# Print out the multiples of 3 up to 100; modulo checks for remainders, so a R == 0 means its a multiple

for count in range (101):
    if count % 3 == 0:
        print (count)
    elif count % 5 == 0:
        print (count)
# Now using the same loop, lets see if we can pint out he multiples of 5 too 
    if count % 5 == 0:
        print (count)
