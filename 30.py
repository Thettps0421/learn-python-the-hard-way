people = 30
cars = 40
strucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if strucks > cars:
    print("That's too many strucks.")
elif strucks < cars:
    print("Maybe we could take the strucks.")
else:
    print("We still can't decide.")

if people > strucks:
    print("Alright, let's just take the strucks.")
else:
    print("Fine, let's stay home then.")