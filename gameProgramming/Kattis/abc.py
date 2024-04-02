#input ints (A, B, C)
#use .split to turn line of numbers into 3 seperate ones
#cast strings to ints
#check for A<B<C

#input order
#create a string for output
#use a for loop to iterate the order
    #if letter is A, add A integer + " " to string
    #if letter is B, add B integer + " " to string
    #if letter is C, add C integer + " " to string
# print the correct order to the screen

a, b, c = input().split()
letterList = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b:
    a, b = b, a
if c < b:
    c, b = b, c
if a > b:
    a, b = b, a

