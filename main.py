import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number!")
print("1 se 100 ke beech ek number socho.")

while True:
    guess = int(input("Apna guess enter karo: "))
    attempts += 1

    if guess > secret_number:
        print("Bohot bada number hai! Chota try karo.")
    elif guess < secret_number:
        print("Bohot chota number hai! Bada try karo.")
    else:
        print(f"Sahi jawab! Aapne {attempts} attempts mein guess kar liya!")
        break