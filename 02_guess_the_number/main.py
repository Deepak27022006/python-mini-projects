import secrets

print("Welcome to the number guess game")

secret_num= secrets.randbelow(20)+1

for attempt in range(1,6):
    guess= int(input(f"Attempt {attempt}: Enter your guess: "))
    
    if guess==secret_num:
        print("🎉 Congratulation, you guess right")
        break
    elif guess < secret_num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")    

else:
    print(f"Better luck next time")         