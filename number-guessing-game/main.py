import random
secret_no = random.randint(1,100)

print("guess no bw 1 to 100")

while True:
    guess_no = int(input("enter no"))
    if guess_no==secret_no:
        print("you guessed the no")
        break
    elif guess_no<secret_no:
        print("higher")
    elif guess_no>secret_no:
        print("lower")

print("GAME OVER")
    
