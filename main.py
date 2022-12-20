# comments

# variables
# name = 'Clever Programmer'
# age = 25

# print(name)
# print(age)

# width, height = 400, 500
# print(width)
# print(height)

# your_name = input('Please enter your name: ')
# print(f'Your name 👉🏼 {your_name}')

# num1 = input('Enter a number: ')
# num2 = input('Enter a number: ')

# print(num1 + num2)

# DATA TYPES
# strings
# int (1,2,3), float (0.2, 2.1) (numbers)

# strings 'hello', 'cookie' 👉🏼 'hellocookie'
# strings '10', '20' 👉🏼 '1020'
# print(int(num1) + int(num2))

# Tip Calculator App
# food_amount = $100
# tip_amount = 20% Tip
# How much am I paying in total?
# food_amount = float(input('Enter food amount $: '))
# tip_percentage = float(input('Enter your tip percentage: ')) / 100
# tip_amount = food_amount * tip_percentage
# # total 👉🏼 food_amount + tip_amount
# total = food_amount + tip_amount
# # string formatting
# print('-------------------------------')
# print(f'Food amount: ${food_amount}')
# print(f'Tip amount: ${tip_amount}\n')
# print(f"Total amount 👉🏼 ${total}")
# print('-------------------------------')

# Boolean
# if then else

# BOOLEAN (True, False)
# comparison operators
# == != > < >= <=


# baby weather app
# if it´s raining outside, grab an umbrella
# otherwise, grab your sunglasses

# weather = input('How is the weather? ')

# if weather == 'rainy':
#     print('☔')
# elif weather == 'cloudy':
#     print('☁')
# elif weather == 'thunderstorm':
#     print('🌩')
# else:
#     print('😎')

# >= 90 👉🏼 A
# >= 80 👉🏼 B
# >= 70 👉🏼 C
# >= 60 👉🏼 D
# < 60  👉🏼 F

# score = int(input('Score: '))

# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')

# if 60 <= score <= 100: # pythonic
#     print('passing grade')
# elif score < 60 or score > 100:
#     print('you either failed or you super passed')

# Functions

def say_my_name():
    print('Rafeh Qazi')

def say_my_name(name):
    print(name)

# say_my_name()
# say_my_name('Lio Messi')

def greeting(name):
    # print('Hey! {}'.format(name))
    print(f'🖖🏼Hey {name}!')

# greeting('Lio Messi')

def greeting(name,greet='Hello'):
    '''
    greeting takes in 2 arguments, greet & name
    and it greets the user.

    👉🏼 greeting('Hey','Rafi')
        🖖🏼Hey Rafi!
    '''
    print(f'🖖🏼{greet} {name}!')

# greeting('Aloha','Lio Messi')
# greeting('Lio Messi')

# named arguments
# greeting(greet='Hey',name='Lio')

def sum(a:int,b:int) -> int:
    '''
    Takes 2 integers, return their sum.
    👉🏼 sum(2,3)
    5
    '''
    return a+b

num = sum(2,3)
# print(num)

### CONVERT THIS INTO A FUNCTION ###
#food_amount = float(input('Enter food amount $: '))
# tip_percentage = float(input('Enter your tip percentage: ')) / 100
# tip_amount = food_amount * tip_percentage
# # total 👉🏼 food_amount + tip_amount
# total = food_amount + tip_amount

def calculateFoodTotal(food: float,tip_percentage:int) -> float:
    tip = food * (tip_percentage / 100)
    total = food + tip
    print('\n')
    print('-------------------------------')
    print(f'Food amount: ${food}')
    print(f'Tip amount: ${tip}\n')
    print(f"Total amount 👉🏼 ${total}")
    print('-------------------------------')
    print('\n')
    return total

# calculateFoodTotal(food=100,tip_percentage=20)

# TYPEHINTING
def weatherToEmoji(weather: str) -> None:
    '''
    weatherToEmoji takes in 1 argument as a string (expected inputs: 'rainy' 'cloudy' 'thunderstorm')

    👉🏼 weatheToEmoji('rainy')
    ☔
    '''
    if weather == 'rainy':
        print('☔')
    elif weather == 'cloudy':
        print('☁')
    elif weather == 'thunderstorm':
        print('🌩')
    else:
        print('😎')

# weatherToEmoji('cloudy')

# Write a function bigger_guy that takes in
# two numbers and returns the bigger one.

def bigger_guy(a:int,b:int) -> int:
    '''
    Given 2 numbers, return the bigger one
    >>>> bigger_guy(2,3)
    3
    '''
    if a > b:
        return a
    return b

# print(bigger_guy(3,2))

# Lambda  - anonymous function
# implicit return
sum2 = lambda a,b: a+b
# print(sum2(1,2))

bigger_guy2 = lambda a,b: a if a > b else b
# print(bigger_guy2(20,10))

greeting2 = lambda greet, name: f'{greet} {name}!'
# print(greeting2('Aloha','Lio'))

# testing your code / unit tests

def test_sum():

    assert sum(1,2) == 3, '❌ sum(1,2) does not return 3 like it should'

    assert sum(-20,20) == 0
    assert sum(20,20) == 40
    assert sum (12,21) == 33

    print('Sum Function: All Tests Passed (4/4) 👌🏼')

# test_sum()

# *********************************************
# List
# methods
fruits = ['🍊','🍌','🍐','🍉','🍒','🍓',]
# print(fruits)
fruits.append('🍏')
# print(fruits)

# INDEXING
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])

#how to ALWAYS get the last item in an array?
# print(fruits[-1])

# Slicing
# print(fruits[0:6]) # 1st inclusive, 2nd exclusive
# print(fruits[1:3])

# Length
# print(len(fruits))
# print(fruits[0:len(fruits)-1])
# print('Hi my name is Qazi'[0:12])

# print(fruits[::-1]) # reverse the array

# fruits = ['🍊','🍌','🍐','🍉','🍒','🍓',12,'Hi',2.2,]

# DICTIONARIES
# key 👉🏼 value
# Mutable

# person = {
#     'name':'Qazi',
#     'shirt':'black',
#     'laptop':'Apple',
# }

# print(person['name'])
# print(person['shirt'])
# print(person['laptop'])

def introducer():
    person = {
    'name':'Qazi',
    'shirt':'black',
    'laptop':'Apple',
    'assets':100,
    'debt':50,
    'netWorth': lambda: person['assets'] - person['debt'],
    'favoriteFruits':['🍊','🍌','🍎'] 
}
    # ☢
    person['name'] = 'Lio' 
    person['shirt'] = 'blue'  
    person['assets'] = 1000 

    print(f"🖖🏼HI my name is {person['name']}, 👕I am wearing a {person['shirt']} shirt, 💻and the laptop I use to code is an {person['laptop']}.\n💰My networth is ${person['netWorth']()} USD.\n🍒My favorite fruits are {person['favoriteFruits']}")

    # print(list(person.keys()))
    # print(list(person.values()))
    # print(list(reversed(person)))

# introducer()

### TUPLES () ###
# immutable
# numbers = (1,2)
# print(numbers)
# print(type(numbers))
# print(numbers[0])

### SETS {} 👉🏼 Used for getting unique stuff ###
list1 = ['ruby','python','js']
list2 = ['ruby','SQL','JAVA','js']

# unique languages
# programming_languages = set(list1 + list2)
# print(programming_languages)
# in Operator
# print('GO' in programming_languages)
# print('SQL' in programming_languages)

# print({1,2,2})
# print(set([1,2,3,4,2,2]))

# def unique(languages):
#     '''
#     Create a function unique, that takes
#     in a list and returns only unique items.
#     >>>> unique(['ruby','ruby','python'])
#     ['ruby','python']
#     '''
#     return list(set(languages))

unique = lambda languages: list(set(languages))
    
# print(unique(['ruby','ruby','python']))

### LOOPS ###
### FOR LOOPS ###
fruits = ['🍊','🍌','🍐','🍉','🍒','🍓',]

# for x in range(len(fruits)):
#     print(f'fruit: {fruits[x]} 👉🏼 {x}')

# for fruit in fruits:
#     print(f'fruit: {fruit} 👉🏼 {fruits.index(fruit)}')

# print(list(enumerate(fruits)))

# # tuple unpacking
# for index, fruit in enumerate(fruits):
#     print(f'fruit: {fruit} 👉🏼 {index}')

# for _ in range(10):
#     print('Aloha')

# for i in range(10):
#     print(fruits)
#     fruits.append('🍎')

### WHILE LOOP ###
# WATCHOUT FOR: 👉🏼 INFINITE LOOP

# counter = 0
# while counter < 10:
#     print(counter)
    # counter = counter + 1
    # counter += 1
    
### EXERCISES ###

def double(numbers: list) -> list:
    '''
    >>>> double([1,2,3,4,5,])
    [2,4,6,8,10]
    '''
    result = []
    for number in numbers:
        result.append(number*2)
    return result 

# print(double([1,2,3,4,5,]))


def count_words(phrase: str) -> int:
    '''
    count_words if given a string, should count & return the numbers of words
    >>>> count_words('Hi my name is Qazi')
    5
    '''
    return len(phrase.split())

# print(count_words('Hi my name is Qazi'))

def sum_list(numbers: list[int]) -> int:
    '''
    Create a function that given a list of numbers, it can return their sum.
    >>>> sum_list([1,2,3])
    6
    '''
    result = 0
    for number in numbers:
        result += number

    return result

# print(sum_list([1,2,3,4]))

def find_max(numbers: list[int]) -> int:
    '''
    >>>> find_max([1,5,10,3])
    10
    '''
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
    
    return current_max

# print(find_max([1,5,10,3]))

def word_frequency(phrase: str):
    '''
    >>>> word_frequency('I love Batman because I am Batman')
    {'I': 2, 'love': 1, 'Batman': 2, 'am': 1, 'because': 1}
    '''
    result = {}
    for word in phrase.split():
        if word not in result:
            result[word] = 1
        else: 
            result[word] += 1

    return result

# # loop 1
# is 'I' in result? no
# set the key to 'I' and value to 1

# # loop 2
# is 'love' in result? no
# set the key to 'love' and value to 1

# # loop 3
# is 'Batman' in result? no
# set the key to 'Batman' and value to 1

# # loop 4
# is 'because' in result? no
# set the key to 'because' and value to 1

# # loop 5
# is 'I' in result? yes
# increment the value of 'I' key by 1

# # loop 6
# is 'am' in result? no
# set the key to 'am' and value to 1

# # loop 7
# is 'Batman' in result? yes
# increment the value of 'Batman' key by 1

# print(word_frequency('I love Batman because I am Batman'))

# print(word_frequency(input('Please enter your phrase: ')))

### HIGHER ORDER FUNCTIONS ###
### map
def double_number(number):
    return number*2

# print(list(map(double_number,[1,2,3])))

# print(list(map(lambda num: num*2,[1,2,3])))
# print(list(map(lambda num: num**2,[1,2,3])))

### filter
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# even numbers
# print(list(filter(lambda num: not num % 2,numbers)))

### LIST COMPREHENSIONS ###

# filter 👉🏼 and give me only the EVEN numbers
# print([number for number in numbers if not number % 2])

# map 👉🏼 double numbers
# print([number * 2 for number in numbers])

# get odd numbers
# print([number for number in [1,3,4,5,6,7,8,12] if number % 2])

# give me all the od numbers cubed
# print([number**3 for number in [1,3,4,5,6,7,8,12] if number % 2])