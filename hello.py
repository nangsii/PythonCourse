print("hello world")
hello = "hello"
name = input("what's your name?\n")
greeting = hello + " " + name + "!"
print(greeting)
age = int(input("how old are you?\n"))
decades = age//10
years = age % 10
print("Wow! that means you are " + str(decades) + " decades and " + str(years) + " years old.")
print("You are so old!")
print("You should be making babies!")
gf = input("Do you have a girlfriend? (yes/no)\n")
condition = gf == "yes"
if condition: 
    print("nice!")
    her_age = int(input("how old is she?\n"))
    if her_age > age:
        print(" oh, she is older than you, you should hurry up and make babies already! ")
    else:
        print("not bad, you still have time to make babies. enjoy your life for now! ")
else:
    print("sad!")


