import os
# r = read
# a = append
# w = Write
# x = create
#  Similar to CRUD

# Read - error if it doesn't exist

f = open("names.txt", "r")

#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File does not exist")
finally:
    f.close


#Append to a file
# creates a file if it doesn't exist

f=open("names.txt","a")
f.write("\nKen Hizer")
f.close()

print("\n")

f=open("names.txt")
print(f.read())

f.close()

#Write (Over-write)

f=open("context.txt", "w")
f.write("\n\nI deleted all context")
f.close()

f=open("context.txt")
print(f.read())
f.close()

#two ways to create a new file
#this opens a file for writing
#this also creates the file if it doesn't exist

f=open("name_list.txt","w")
f.close()

#creates the specified file but returns an error if it exists
if not os.path.exists("dave.txt"):
    f= open("dave.txt","x")
    f.close()


#delete a file, avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("the file does not exist")


with open("more_names.txt") as f:
    content=f.read()

with open("names.txt","w") as f:
    f.write(content)
