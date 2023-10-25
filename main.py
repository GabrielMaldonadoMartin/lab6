def encode(password):
    global newPass
    newPass =  ""
    for i in password:
        if i == '7':
            newPass += '0'
        elif i == '8':
            newPass += '1'
        elif i == '9':
            newPass += '2'
        else:
            newPass += str(int(i) + 3)
    print('Your password has been encoded and stored!\n')

if __name__ == "__main__":
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        choice = input('Please enter an option: ')
        if choice == '1':
            encode(input('Please enter your password to encode: '))
            print(newPass)
        # elif choice == '2':
            # decode() goes in here :)
        else:
            break