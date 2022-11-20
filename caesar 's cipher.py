import random

def all_chars_and_parameters():
    output = []
    all_chars = ''

    digits = '1234567890'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    punctuation = '!#$%&*+-=?@^_'

    print('Сколько паролей нужно?')
    output.append(int(input()))

    print('Какая длина пароля?')
    output.append(int(input()))

    print('Нужны ли в пароле цифры?')
    if input() == 'да':
        all_chars += digits

    print('Нужны ли маленькие буквы?')
    if input() == 'да':
        all_chars += lowercase_letters

    print('Нужны ли большие буквы?')
    if input() == 'да':
        all_chars += uppercase_letters
    
    print('Нужны ли символы?')
    if input() == 'да':
        all_chars += punctuation

    print('Нужны ли неоднозначные символы?')
    if input() == 'нет':
        all_chars = all_chars.replace('0', '')
        all_chars = all_chars.replace('o', '')
        all_chars = all_chars.replace('O', '')
        all_chars = all_chars.replace('1', '')
        all_chars = all_chars.replace('i', '')
        all_chars = all_chars.replace('l', '')
        all_chars = all_chars.replace('L', '')

    return output, all_chars

def generate_password(lenght, chars):
    output = ''

    for _ in range(lenght):
        symbol = random.choice(chars)
        output += symbol
    
    return output

output_first = all_chars_and_parameters()
chars = output_first[1]

for _ in range(output_first[0][0]):
    print(generate_password(output_first[0][1], chars))