
fruits_data = 'apple,avocado,banana,cantaloupe,grapefruit,grapes,honeydew melon,kiwifruit,lemon,lime,nectarine,orange,peach,pear,pineapple,plums,strawberries,sweet cherries,tangerine,watermelon'
fruits = fruits_data.split(',')
calories= [130,50,110,50,60,90,50,90,15,20,60,80,60,100,50,70,50,100,50,80]
info_dict = {fruit:calorie for fruit,calorie in zip(fruits,calories)}
def request():
    usrinput = input('Item: ')
    if usrinput.lower() in info_dict:
        return print('Calories:', info_dict[usrinput.lower()])
    else:
        return print('Not Available')
request()