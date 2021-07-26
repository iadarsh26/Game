import random
import time

Plangs = ("python", "php", "javascript", "perl","java", "ruby"
          , "cobol", "fortran", "pascal", "basic", "swift")

answer = random.choice(Plangs)

correct = answer

rumble = ""

print("\nLet's play")

while answer:
    position = random.randrange(len(answer))
    rumble += answer[position]
    answer = answer[:position] + answer[(position + 1):]

start_time = time.perf_counter() 
print("The Word Is:" ,rumble)

guess = input("Guess This Programming Language:- ")
guess = guess.lower()

while (guess != correct) or (guess == ""):
    print("That is not the correct answer")
    guess = input("Guess This Programming Language:- ")
    guess = guess.lower()
    
if guess == correct:
    print("\nCongratulation Correct answer!")
    print("\n--- %s seconds ---" % (time.perf_counter() - start_time))
    input("\n Press any to Exit!")    