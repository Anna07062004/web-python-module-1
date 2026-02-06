import random

def generate_number():
    digits = random.sample('0123456789', 4)
    return "".join(digits)

def count_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    return bulls, cows

def game_loop(secret, attempts=0):
    guess = input("Введите 4-значное число: ").strip()
    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите ровно 4 цифры.")
        return game_loop(secret, attempts) 
    
    if guess == secret:
        attempts += 1
        print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
        return 
    
    bulls, cows = count_bulls_and_cows(secret, guess)
    print(f"Быки: {bulls}, Коровы: {cows}")
    game_loop(secret, attempts + 1)

def main():
    print("Добро пожаловать в игру «Быки и коровы»!")
    print("Я загадал 4-значное число. Попробуйте его угадать.")
    print("Быки — сколько цифр есть в числе (не на своём месте).")
    print("Коровы — сколько цифр на своём месте.\n")
    
    secret_number = generate_number()
    game_loop(secret_number)
if __name__ == "__main__":
    main()