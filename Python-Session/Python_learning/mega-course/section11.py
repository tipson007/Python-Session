#def greetings(name, surname):
 #   name = input("Enter your name: ")
 #   surname =  input("Enter your surname: ")
#   message = f"Hi {name} {surname}"
#print(greetings)


#best practice to read a file
with open("files/fruits.txt") as myfile:
    content = myfile.read()

print(content)

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato\nCocumber\nOnion")

def foo(character, filepath="fruits.txt"):
    with open(filepath) as myfile:
        content = myfile.read()
    return content.count(character)

#Cheatsheett (File Processing)
#In this section, you learned that:

#You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()
#You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")
#You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")
#You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()