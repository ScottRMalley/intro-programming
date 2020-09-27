import sys

if(len(sys.argv) < 2):
    print('Please input a word')
else:
    word = sys.argv[1]
    is_palindrome = True
    for i in range(len(word)//2):
        if not (word[i] == word[len(word)-i-1]):
            is_palindrome = False

    if is_palindrome:
        print(word + ' is a palindrome')
    else:
        print(word + ' is not a palindrome')
