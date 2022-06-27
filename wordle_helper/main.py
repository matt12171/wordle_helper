alpha = 'abcdefghijklmnopqrstuvwxyz'
words_list = list()
words_list_5 = list()

chars = {}

char_lists = {
    1: list(),
    2: list(),
    3: list(),
    4: list(),
    5: list(),
}

print(''' 
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |  _________   | || |   _____      | || |   ______     | || |  _________   | || |  _______     | |
| | |_   ||   _| | || | |_   ___  |  | || |  |_   _|     | || |  |_   __ \   | || | |_   ___  |  | || | |_   __ \    | |
| |   | |__| |   | || |   | |_  \_|  | || |    | |       | || |    | |__) |  | || |   | |_  \_|  | || |   | |__) |   | |
| |   |  __  |   | || |   |  _|  _   | || |    | |   _   | || |    |  ___/   | || |   |  _|  _   | || |   |  __ /    | |
| |  _| |  | |_  | || |  _| |___/ |  | || |   _| |__/ |  | || |   _| |_      | || |  _| |___/ |  | || |  _| |  \ \_  | |
| | |____||____| | || | |_________|  | || |  |________|  | || |  |_____|     | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  


''')
print('Welcome to wordle helper')
print('')
print('Enter any green character you have in the correct space numbered 1-5. The program will then ask for any yellow characters and then any black characters (characters it can\'t be).')
print('''

    Some basic rules - 

    - Only enter 1 character at a time. Multiple will cause errors. 
    - Please enter letters in lowercase or it will return unexpected results. I could fix this in roughly 30 seconds but cba so just do it. 
    - You should run the program every guess.
    - This doesn't make you good at wordle. This is cheating and should be used for fun/saving 2 hours on an excel spreadsheet. 


''')

status = True

while status:
    # Takes words from words.txt and adds them to a list
    with open('words.txt') as file_object:
        file_data = file_object.readlines()

        for word in file_data:
            word = word.strip()
            word = word.lower()

            if len(word) == 5 and word.isalpha():
                words_list_5.append(word)

    # Added while loops for user input errors
    print('If you don\'t know the letter then enter =')

    while True:
        guess = input('Enter full guess. Replace yellow/black characters with "=": ').lower()

        parsed = True

        if len(guess) == 5:
            for i in range(5):
                if guess[i] not in alpha and guess[i] != '=':
                    parsed = False

                chars[i] = guess[i]

            if parsed:
                break
            else:
                chars = {}

        if len(guess) != 5 or not parsed:
            print('')
            print('Your guess must be 5 latin characters or "=" for spots without confirmed letters')
            print('')

    for i in range(5):
        # goes through word list and adds words beginning with char to list
        if chars[i] != '=':
            for word in words_list_5:
                if chars[i] == word[i]:
                    char_lists[i].append(word)

            # Clear list and add new words
            # Needs to be done so that if the 1st char is left blank then the 2nd char choice won't search a blank list
            words_list_5.clear()

            for words in char_lists[i]:
                words_list_5.append(words)

    black_letters = input('Black characters: ').lower()

    for k, black_letter in enumerate(black_letters):
        matches = list()

        for word in words_list_5:
            if black_letter not in word:
                matches.append(word)

        words_list_5 = matches

    yellow_letters = input('Yellow characters: ').lower()

    for k, yellow_letter in enumerate(yellow_letters):
        matches = list()

        for word in words_list_5:
            if yellow_letter in word:
                matches.append(word)

        words_list_5 = matches

    print(words_list_5)

    decide = input('Do you want to start again? (y/n): ').lower()

    if decide == 'n':
        print('')
        print('Thanks for using my program')
        print('')
        status = False
