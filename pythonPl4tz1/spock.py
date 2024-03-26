user_option = 'spock'  # User
computer_option = input(
    ' Computer' '\n' 'piedra, papel, tijera, lagarto o spock => ')
'''
Tijera corta a papel
y como siempre, piedra aplasta a tijera”

tijera decapita a lagarto
Spock rompe a tijera

papel tapa a piedra
lagarto devora a papel

papel desautoriza a Spock
piedra aplasta a lagarto
Spock vaporiza a piedra
'''


if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'papel':
        print('Papel cubra piedra''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Piedra aplasta a lagarto''\n''User gana!')
    if computer_option == 'spock':
        print('Spock pulperiza piedra''\n''Computer gana!')
    if computer_option == 'tijera':
        print('Piedra rompe tijera''\n''User gana!')
elif user_option == 'papel':
    if computer_option == 'tijera':
        print('Tijera rompe papel''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Lagarto devora papel''\n''Computer gana!')
    if computer_option == 'spock':
        print('Papel desautoriza a Spock''\n''User gana!')
    if computer_option == 'piedra':
        print('Papel envuelve piedra''\n''User gana!')
elif user_option == 'tijera':
    if computer_option == 'piedra':
        print('Piedra rompe tijera''\n''Computer gana!')
    if computer_option == 'papel':
        print('Tijera rompe papel''\n''User gana!')
    if computer_option == 'spock':
        print('Spock rompe tijeras''\n''Computer gana!')
    if computer_option == 'lagarto':
        print('Tijera decapita lagarto''\n''User gana!')
elif user_option == 'lagarto':
    if computer_option == 'piedra':
        print('Piedra aplasta lagarto''\n''Computer gana!')
    if computer_option == 'papel':
        print('Lagarto como papel''\n''User gana!')
    if computer_option == 'tijera':
        print('Tijera decapita lagarto''\n''Computer gana!')
    if computer_option == 'spock':
        print('Lagarto envenena spock''\n''User gana!')
elif user_option == 'spock':
    if computer_option == 'piedra':
        print('Spock vaporiza a piedra''\n''User gana!')
    if computer_option == 'papel':
        print('Papel dezautoriza a Spock''\n''Computer gana!')
    if computer_option == 'tijera':
        print('Spock rompe tijera''\n''User gana!')
    if computer_option == 'lagarto':
        print('Lagarto envenena a Spock''\n''Computer gana!')