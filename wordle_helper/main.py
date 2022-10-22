def main():

    # Returns list of 5 letter words
    words_list = open_file('words5.txt')

    while True:
        count = 0
        user = input('Enter word guessed: ')
        while len(user) != 5 or user.isalpha() == False:
            print('Input must be 5 letters')
            user = input('Enter word guessed: ')
        
        user = user.lower()

        for letter in user:
            words_list = letter_check(letter, words_list, count)
            count +=1
        print(words_list)
        
        loop = input('Guess again? y/n: ')
        while loop != 'y' and loop != 'n':
            print('Enter either y or n')
            loop = input('Guess again? y/n: ')
        if loop == 'n':
            break
            
# Checks each letter
def letter_check(letter, words_list, index):
    user = input(f'Was letter "{letter}" b/y/g: ')
    while user != 'b' and user != 'y' and user != 'g':
        print('Input must be b/y/g')
        user = input(f'Was letter "{letter}" b/y/g: ')
    
    # BLACK LETTERS
    if user == 'b':
        for i in range(len(words_list)):
            for word in words_list:
                if letter in word:
                    words_list.remove(word)

    # YELLOW LETTERS            
    elif user == 'y':
        for word in words_list:
            if letter == word[index]:
                words_list.remove(word)
        for i in range(len(words_list)):   
            for word in words_list:
                if letter not in word:
                    words_list.remove(word)

    # GREEN LETTERS
    elif user == 'g':
        for i in range(len(words_list)):
            for word in words_list:
                if letter != word[index]:
                    words_list.remove(word)

    return(words_list)

def open_file(file_name):
        words_list = []
        with open(file_name) as file:
            file_data = file.readlines()
            for words in file_data:
                words = words.strip()
                words_list.append(words)
        return words_list

if __name__ == '__main__':
    main()
