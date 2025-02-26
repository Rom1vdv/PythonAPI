import random

print("Enter floor number") 
firstNumber = int(input())
print("Enter ceiling number") 
secondNumber = int(input())
answer = random.randint(firstNumber, secondNumber)
match = False
while match == False:
	guess = int(input())
	if guess == answer:
		match = True
	print("Wrong on gromo")
print(f"You found the right answer, it was {answer}")