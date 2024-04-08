options = ('piedra', 'papel', 'tijera')

user_option = input('piedra, papel o tijera =>')
user_option = user_option.lower()
computer_option = 'piedra'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('')