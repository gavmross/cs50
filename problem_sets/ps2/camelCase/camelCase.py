CAMEL CASE
camelCase = input('camelCase: ')
snake_case = camelCase
upperLetters = []
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        upperLetters.append(camelCase[i])
for letter in upperLetters:
    snake_case = snake_case[:snake_case.find(letter)] + '_'+ snake_case[snake_case.find(letter):]
snake_case = snake_case.lower()
print('snake_case: ', snake_case)