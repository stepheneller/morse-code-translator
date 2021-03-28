# International morse code translator

# Rules for international morse code
# 1. The length of a dot is one unit
# 2. A dash is three units
# 3. The space between parts of the same letter is one unit
# 4. The space between letters is three units
# 5. The space between words is seven units

# English to morse code dictionary
from dicts import text_to_morse_code_dict

# Morse code to english dictionary
from dicts import morse_code_to_english_dict


# Asks for the users input on whether they want to translate English to Morse Code or Morse Code to English.
def start():
    morse_or_english = str(input('Would you like to translate into Morse Code or English?: ')).lower()

    if morse_or_english == 'morse code':
        print("You've chosen to convert English into Morse Code.")
        continue_translation = str(input("Press Y to continue or N to go back: ")).upper()
        if continue_translation == 'Y':
            print("Continuing...")
            english_to_morse_code()
        else:
            print("Going back...")
            start()

    elif morse_or_english == 'english':
        print("You've chosen to convert Morse Code into English.")
        continue_translation = str(input("Press Y to continue or N to go back: ")).upper()
        if continue_translation == 'Y':
            print("Continuing...")
            morse_code_to_english()
        else:
            print("Going back...")
            start()

    else:
        print("Please input either 'Morse Code' or 'English' to continue.")
        start()


# Translates English to Morse Code
def english_to_morse_code():
    space = '   '
    converted_word = ''
    word_to_translate = str(input("Please enter a word to be converted into Morse Code: "))
    continue_translation = str(input(f"Your word is '{word_to_translate}' continue? enter Y or N: ")).upper()

    if continue_translation == 'Y':
        split_word_to_translate = word_to_translate.upper().split(' ')
        for word in split_word_to_translate:
            word_length = len(word)
            for num in range(0, word_length):
                if num < word_length - 1:
                    converted_word += text_to_morse_code_dict[word[num]] + space
                elif num == word_length - 1:
                    converted_word += text_to_morse_code_dict[word[num]]

            converted_word += text_to_morse_code_dict[' ']

        print("Your text in Morse Code is: ")
        print(converted_word)

        again = str(input("Would you like to translate something else?: enter Y or N: ")).upper()

        if again == 'Y':
            start()
        else:
            print("Goodbye!")

    elif continue_translation == 'N':
        english_to_morse_code()

    else:
        print("Could not understand input...")
        start()


# Translate Morse Code to English
def morse_code_to_english():
    decoded_word = ''
    space = '   '
    morse_code_to_translate = str(input("Please enter the Morse Code to be converted into English: \n"))
    continue_translation = str(input(f"Your code is '{morse_code_to_translate}' continue? enter Y or N: \n")).upper()

    if continue_translation == 'Y':
        morse_code_word_split = morse_code_to_translate.split(text_to_morse_code_dict[' '])[:-1]
        for code in morse_code_word_split:
            split_code = code.split(space)
            for morse_code in split_code:
                decoded_word += morse_code_to_english_dict[morse_code]

            decoded_word += morse_code_to_english_dict[' ']

        print("Your decoded word is:")
        print(decoded_word)

        again = str(input("Would you like to translate something else?: enter Y or N: ")).upper()

        if again == 'Y':
            start()
        else:
            print("Goodbye!")

    elif continue_translation == 'N':
        morse_code_to_english()

    else:
        print("Could not understand input...")
        start()


start()
