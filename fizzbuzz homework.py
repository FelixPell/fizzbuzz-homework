print("Hello! What is your name? ")
myName = input()
print("Nice to meet you, " + myName + "! Please do me the favour and choose a number between 1 and 100! ")

choice = input()
choice = int(choice)

for fizzbuzz in range(1, choice):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

print("That's it, " + myName + ". I hope you enjoyed the show! ")