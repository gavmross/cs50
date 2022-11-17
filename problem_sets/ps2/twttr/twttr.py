def main():
    word = input('Input: ')
    print(shorten(word))

def shorten(word):
    output = word
    vowels = 'AEIOUaeiou'
    for letter in word:
        if letter in vowels:
            output = output.replace(letter,'')
    return output

if __name__ == '__main__':
    main()