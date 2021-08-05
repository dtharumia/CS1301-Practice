# from math import *

# print('dharshan')

# msg = "this is a message as a variable"

# print(msg)

# player_one = 'dharshan'

# print("The first player is", player_one)
# print("it is good to meet you " + player_one + ". I hope you enjoy your stay")
# print("Hello %s" % player_one)
# print("Hi {}".format(player_one))
# print(f"Hey {player_one}")

# print("Dharshan\nTharumia")

# print(player_one.upper())

# name = "alexander"

# print(name[::-1])

# print(name.index("x"))

# print(floor(43.234234234))

# name = input('what is your name? ')

# print(f"hello, {name}")

# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# result = float(num1)+float(num2)
# print(result)

# color = input("Please choose a color: ")
# plural_noun = input("Please choose a plural noun: ")
# celebrity = input("Please choose a celebrity: ")
# # num = 11
# # print("that's nice {}".format(num))

# print("Roses are {}".format(color))
# print("{} are blue".format(plural_noun))
# print("I love {}".format(celebrity))

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# # print(colors[0], colors[3])
# colors[0] = 'roy'
# # print(colors[::-1])
# fruits = ['apple', 'banana', 'orange']
# colors.extend(fruits)
# print(colors)
# colors.append(fruits[0])
# colors.insert(2, fruits[1])
# print(colors)
# last = colors.pop()
# print(last)

# coordinates = (3, 4)
# print(coordinates[0])

# def greet(greeting):
#     print(greeting)

# greet("hey")

# def cube(num):
#     return num**3

# print(cube(2))

# is_male = True
# is_tall = False

# if(not(is_male)):
#     print('you\'re a male')
# elif(is_male and not(is_tall)):
#     print('you are a male but not tall')
# else:
#     print('you\'re not a male')


# def max_num(*args):
#     sum = 0
#     sum += args
#     return sum

# max_num(1, 2, 3)

# monthConversions = {
#     'Jan': 'January',
#     'Feb': 'February',
#     'Mar': 'March',
#     'Apr': 'April',
#     'May': 'May',
#     'Jun': 'June',
#     'Jul': 'July',
#     'Aug': 'August',
#     'Sep': 'September',
#     'Oct': 'October',
#     'Nov': 'November',
#     'Dec': 'December'
# }

# print(monthConversions.get("Jul", "Not a valid key"))

# i = 1

# while i <= 10:
#     print('hi')
#     i += 1

# for x in range(0, 2):
# print('bye', x)

# secret_word = "panda"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Please guess the secret word ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses, you lose!")
# else:
#     print("You win!")

# for letter in "Giraffe Academy":
#     print(letter)

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result*base_num
#     return result


# print(raise_to_power(3, 5))

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# print(number_grid[1][1])

# for row in number_grid:
# for col in row:
#     print(col)


# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation


# print(translate(input("Enter a phrase: ")))
# try:
#     value = 10/0
#     number = int(input("Enter a number "))
#     print(number)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError:
#     print("Invalid input")
# print('later')

# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# employee_file = open("employees.txt", "w")
# employee_file.write("\nDharshan - Programmer")
# employee_file.close()

# import useful_func

# useful_func.greet('bob')

# from Student import Student

# student1 = Student('John', 'Engineering', 3.8, False)

# print(student1.on_honor_roll())

# print(student1.name)

# from Question import Question

# question_prompts = [
#     "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
# ]

# questions = [
#     Question(question_prompts[0], 'a'),
#     Question(question_prompts[1], 'c'),
#     Question(question_prompts[2], 'b'),
# ]


# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print(f"You got {score}/{len(questions)} correct")

# run_test(questions)

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChineseChef = ChineseChef()

myChef.make_chicken()

myChineseChef.make_salad()

myChineseChef.make_fried_rice()
