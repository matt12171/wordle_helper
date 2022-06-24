alpha = 'abcdefghijklmnopqrstuvwxyz'
words_list = list()
words_list_5 = list()
char_1_list = list()
char_2_list = list()
char_3_list = list()
char_4_list = list()
char_5_list = list()

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

while status == True:
    
    # A search function if the user has orange letters
    def yellow_letter(words_list_5):
        char_list = list()
        while True:
            char = input('Enter an yellow character: ').lower()
            if len(char) == 1 and char in alpha:
                break
            else:
                print('Please only input 1 character at a time and make sure it is a letter.')
        for words in words_list_5:
            if char in words:
                char_list.append(words)
        words_list_5.clear()
        for words in char_list:
            words_list_5.append(words)
        return words_list_5
    
    # Removes words that contain certain letters
    def black_letter(words_list_5):
        char_list = list()
        # Adding a loop to check for character length
        while True:
                char = input('Enter a black character: ').lower()
                if len(char) == 1 and char in alpha:
                    break
                else:
                    print('Please only input 1 charater at a time and make sure it is a letter.')
        for words in words_list_5:
            if char not in words:
                char_list.append(words)
        words_list_5.clear()
        for words in char_list:
            words_list_5.append(words)
        return words_list_5
        
    
            

            
            
    


    # Takes words from words.txt and adds them to a list
    with open('words.txt') as file_object:
        file_data = file_object.readlines()
        for words in file_data:
            words2 = words.strip()
            words_list.append(words2)

    for words in words_list:
        if len(words) == 5:
            words_list_5.append(words)
    # converts whole list to lowercase
    for i in range(len(words_list_5)):
        words_list_5[i] = words_list_5[i].lower()

    # Added while loops for user input errors
    print('If you don\'t know the letter then enter =')
    while True:
        char_1 = input('1st character?: ').lower()
        if char_1 in alpha and len(char_1) == 1 or char_1 == '=':
            break
        else:
            print('')
            print('Please only enter 1 letter or \'=\' if you don\'t know')
            print('')
    
    while True:
        char_2 = input('2nd character?: ').lower()
        if char_2 in alpha and len(char_2) == 1 or char_1 == '=':
            break
        else:
            print('')
            print('Please only enter 1 letter or \'=\' if you don\'t know')
            print('')
    
    while True:
        char_3 = input('3rd character?: ').lower()
        if char_3 in alpha and len(char_3) == 1 or char_1 == '=':
            break
        else:
            print('')
            print('Please only enter 1 letter or \'=\' if you don\'t know')
            print('')
    
    while True:
        char_4 = input('4th character?: ').lower()
        if char_4 in alpha and len(char_4) == 1 or char_1 == '=':
            break
        else:
            print('')
            print('Please only enter 1 letter or \'=\' if you don\'t know')
            print('')
    
    while True:
        char_5 = input('5th character?: ').lower()
        if char_5 in alpha and len(char_5) == 1 or char_1 == '=':
            break
        else:
            print('')
            print('Please only enter 1 letter or \'=\' if you don\'t know')
            print('')


    # goes through word list and adds words beginning with char to list
    if char_1 != '=':
        for words in words_list_5:
            if char_1 == words[0]:
                char_1_list.append(words)
    # clears list and adds the new words. This has to be done so that if the 1st char is left blank then the 2nd char choice won't search a blank list. 
        words_list_5.clear()
        for words in char_1_list:
            words_list_5.append(words)

    if char_2 != '=':
        for words in words_list_5:
            if char_2 == words[1]:
                char_2_list.append(words)
        words_list_5.clear()
        for words in char_2_list:
            words_list_5.append(words)

    if char_3 != '=':
        for words in words_list_5:
            if char_3 == words[2]:
                char_3_list.append(words)
        words_list_5.clear()
        for words in char_3_list:
            words_list_5.append(words)

    if char_4 != '=':
        for words in words_list_5:
            if char_4 == words[3]:
                char_4_list.append(words)
        words_list_5.clear()
        for words in char_4_list:
            words_list_5.append(words)

    if char_5 != '=':
        for words in words_list_5:
            if char_5 == words[4]:
                char_5_list.append(words)
        words_list_5.clear()
        for words in char_5_list:
            words_list_5.append(words)


    # Enter any black characters that cannot be in the word

    def ask_for_black():
        # Making sure user can only enter y or n
        while True:
            user_ask = input('Do you have any black characters? (Enter y or n): ').lower()
            if user_ask == 'y' or user_ask == 'n':
                break
            else:
                print('Enter either \'y\' or \'n\'')
                
        if user_ask == 'y':
            # Using a while loop with a try and expect to stop user errors breaking code
            while True:
                try:
                    how_many = input('How many black letters do you have?: ')
                    how_many = int(how_many)
                    break
                except:
                    print('')
                    print('Please input a number dummy')
                    print('')
            while how_many > 0:
                how_many -= 1
                black_letter(words_list_5)
            print(words_list_5)
        elif user_ask == 'n':
            print(words_list_5)
            



    # Uses a count to determine how many times to ask for a yellow letter 
    def ask_for_yellow():
        # Making sure user can only enter y or n
        while True:
            user_ask = input('Do you have any yellow characters? (Enter y or n): ').lower()
            if user_ask == 'y' or user_ask == 'n':
                break
            else:
                print('Enter either \'y\' or \'n\'')      
        if user_ask == 'y':
            # Using a while loop with a try and expect to stop user errors breaking code
            while True:
                try:
                    how_many = input('How many yellow letters do you have?: ')
                    how_many = int(how_many)
                    break
                except:
                    print('')
                    print('Please input a number dummy')
                    print('')
            while how_many > 0:
                how_many -= 1
                yellow_letter(words_list_5)
            

    ask_for_yellow()
    ask_for_black()

    decide = input('Do you want to start again? (y/n)').lower()
    if decide == 'n':
        print('')
        print('Thanks for using my program')
        print('')
        status = False














