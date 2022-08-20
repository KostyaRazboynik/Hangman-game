from hangman.game import Game
from hangman.game_status import GameStatus


def chars_list_to_str(lst):
    return ' '.join(lst)


game = Game()
word = game.generate_word()

letters_count = len(word)

print(f'Слово состоит из {letters_count} букв.\nПопытайся угадать слово (буква за буквой).\n')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input("Введи букву.\n")
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f'Оставшиеся попытки = {game.remaining_tries}')
    print(f'Использованные буквы: {chars_list_to_str(game.tried_letters)}\n')

if game.game_status == GameStatus.LOST:
    print('Тебя повесили!')
    print(f'Загаданное слово было: {game.word}')
else:
    print('Поздравляю! Ты выиграл!')