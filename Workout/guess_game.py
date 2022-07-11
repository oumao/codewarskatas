from random import randint

choice = randint(1, 5)

while True:
    guess = int(input())
    if guess != choice:
        print("Wrong Answer. Try Again")
        continue 
    else:
        print(f"Correct! The answer is {choice}")
        break
