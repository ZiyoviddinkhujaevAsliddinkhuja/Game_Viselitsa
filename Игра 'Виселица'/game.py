import random

WORDS = ['python', 'django', 'javascript', 'php', 'java', 'developer']

def choose_word():
    return random.choice(WORDS)

def initialize():
    word = choose_word()
    guessed_letters = set()
    popitki_otv = 6
    return word, guessed_letters, popitki_otv

def display(word, guessed_letters, popitki_otv):
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print(f'Слово: {display_word}')
    print(f'Осталось попытки: {popitki_otv}')

def user_input():
    user = input("Введите букву: ").lower()
    return user

def update(word, guessed_letters, popitki_otv, user):
    if user in word:
        guessed_letters.add(user)
    else:
        popitki_otv -=1
    return guessed_letters, popitki_otv

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def check_loss(popitki_otv):
    return popitki_otv <= 0

def main():
    word, guessed_letters, popitki_otv = initialize()
    while True:
        display(word, guessed_letters, popitki_otv)
        user = user_input()
        guessed_letters, popitki_otv = update(word,guessed_letters,popitki_otv, user)

        if check_win(word,guessed_letters):
            print(f'Поздравляю! Вы угадали слово: {word}')
            break

        if check_loss(popitki_otv):
            print(f'Вы проиграли! Заданное слово было: {word}')
            break

    if input('Хотите сыграть ещё раз? (да/нет): ').lower() == 'да':
        main()

if __name__ == "__main__":
    main()