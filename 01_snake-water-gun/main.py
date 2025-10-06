import random

print("🐍💧🔫 Welcome Snake, Water, Gun Game 🐍💧🔫")

choices= ["Snake", "Water", "Gun"]

user_choice= input("user choice(Snake,Water,Gun): ").capitalize()

computer=random.choice(choices)
print(f"Computer Choice: {computer}")

if(user_choice not in choices):
    print("⚠️ Invalid choice! Please type Snake, Water, or Gun.")
    exit()

if(user_choice==computer):
    print("⚖️ It's Draw")

elif(user_choice=="Snake" and computer=="Water") or \
    (user_choice=="Water" and computer=="Gun") or \
    (user_choice=="Gun" and computer=="Snake"):
    print("User Wins 🎉")

elif (user_choice not in choices):
    print("You entered wrong choice!")

else:
    print("Computer Wins 💻")
