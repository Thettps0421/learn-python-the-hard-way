from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

program = input("What program do you use? ")

#print("The script is called:", stuff)
#print("Your first variable is:", things)
#print("Your second variable is:", that)
#print("Your third variable is:", thirds)



print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second, f"{program}")
print("Your third variable is:", third)

print(argv)
