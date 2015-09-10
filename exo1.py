
#===============================================================
# Q1: Define an integer variable called a with value 1

# ... your answer
a = 1

# Checking
assert (type(a) == int), "a is not an integer !"
assert (a == 1), "a is not equal to 1 !"
print("Q1 : OK !")


#===============================================================
# Q2: Define two lists l1 and l2
#     l1 : contains the first five elements of li
#     l2 : contains the last  five elements of li
# PS : use list operations and not cheats like l1 = [0, 1, 2, 3, 4]

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ... your answer
l1 = li[:5]
l2 = li[5:]

# Checking  # this is a dirty one :P
assert (str(l1) == "[0, 1, 2, 3, 4]"), "l1 is not well defined !"
assert (str(l2) == "[5, 6, 7, 8, 9]"), "l2 is not well defined !"
print("Q2 : OK !")



#===============================================================
# Q3: Using a for loop, put the first natural integers in l3 (starting from 0)
l3 = []

# ... your answer
for x in range(0, 5):
    l3.append(x)

# Checking
assert (str(l3) == "[0, 1, 2, 3, 4]"), "l3 is not well defined !"
print("Q3 : OK !")


#===============================================================
# Q4: Using a while loop, put the first natural integers in l4 (starting from 0)
l4 = []

# ... your answer
x = 0
while x < 5:
    l4.append(x)
    x += 1

# Checking
assert (str(l4) == "[0, 1, 2, 3, 4]"), "l4 is not well defined !"
print("Q4 : OK !")




#===============================================================
# The end
print("Well done !")
