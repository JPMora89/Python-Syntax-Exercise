def uppercase_words(words):
    for word in words:
        print(word.upper()) 


def print_upper_words(words):
    for word in words:
        print(word.upper())


def print_upper_words_starting(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words_starting_with(words, starts_with):
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words_starting_with(['hello','goodbye', 'elephant', 'tiger', 'lion'], 'h')

