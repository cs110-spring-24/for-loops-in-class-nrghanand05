import random 
ones = 0 
twos = 0 
threes = 0 
fours = 0 
fives = 0 
sixes = 0 
for rolls in range (101):
    dice = random.randint(1,6)
    if (dice == 1): 
        ones +=1
    elif (dice == 2):
        twos +=1
    elif (dice == 3):
        threes +=1
    elif (dice == 4):
        fours +=1
    elif (dice == 5):
        fives +=1 
    else: 
        sixes +=1
    print (dice)
print (f"After 100 rolls, we rolled {ones} 1s, {twos} 2s, {threes} 3s, {fours} 4s, {fives} 5s, and {sixes} 6s.")