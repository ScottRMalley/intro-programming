import sys

def is_palindrome(word):
    return word[::-1] == word

if __name__ == '__main__':
    word = input('Please enter a word: ')
    if(len(word) < 1):
        print('no word entered')
        sys.exit()
    
    print('{} is a palindrome: {}'.format(word, is_palindrome(word.lower())))
