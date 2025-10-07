🎯 Guess the Number Game (1 to 20, 5 Attempts Only – Using secrets)
📌 Description:

This is a fun and interactive Python mini-game where the player must guess a secret number between 1 and 20, but with a twist — you only have 5 attempts to guess it correctly. The game uses Python’s secrets module to generate a secure random number, making it less predictable and more challenging.

🔐 Why Use the secrets Module?

Unlike the random module, the secrets module generates cryptographically secure numbers. While it’s typically used for sensitive data like passwords, it can also add extra unpredictability to simple games — making them more fun!

⚙️ How the Game Works:

The program securely generates a random number from 1 to 20 using secrets.randbelow(20) + 1.

The user has 5 chances to guess the number.

After each guess:

The game tells you if your guess is too high, too low, or correct.

If you guess correctly, the game ends with a success message.

If you use all 5 attempts without guessing correctly, the game ends and reveals the number.
