#slicing in python

alphabet = "qwertyuiopasdfghjklzxcvbnm"
string0 = "Type @ random string"
string1 = "Type anothe/ random str!ng"
string3 = "Third Randomiz3d string%"

#python treats strings like lists
print(alphabet[0]) #what letter prints? q
print(alphabet[-1]) # what letter prints? m

#slice operator :
# syntax  stringName[start:stop]
#start = inclusive, slice includes value
#stop = exclusive, slice will stop before this value

print(alphabet[4:12])# what letters print? r through a

#make a slice using another string. start 5, stop 11

print(string1[5:11]) #what will print? space - r

#slice to the end
print(string1[4:])#start from start value, slice to end of string

#slice from the start
print(string1[:12])#start at beginning, stop one before stop value

#slice whole string
print(string1[:])

#negative slices
print(alphabet[-7:-2])

#password verification
if password[:-1] == " ":
    password = password[:-1]

#removing uneeded information
name = Mr.Sqidward
if name[1:4] == "Mrs.":
    name = name[5:]
elif name[1:3] == "Mr.":
    name = name[4:]