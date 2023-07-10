# Задача 001. Предложите пользователю ввести его имяи выведите 
# приветственное сообщение.Hello [имя]
# print("Hello, ", input("What's your name? "))

# Задача 002. Предложите пользователю ввести его имя и фамилию, 
# после чего выведите приветственное сообщение.Hello [имя] [фамилия].
# print("Hello, ", input("What's your name? "), input("What's your last name? "))

# Задача 003. Напишите код, который выводит вопрос: «What do you call a bear with no teeth?»,
# а в следующей строке выводит ответ: «A gummy bear!» 
# Попробуйте обойтись одной строкой кода
# print("what do you call a bear with no teeth?\nAgummy bear" )

# Задача 004. Предложите пользователю ввести два числа. 
# Сложите эти числа и выведите результат в виде The total is [результат]
# first_num =int(input("Input the first number - "))
# second_num =int(input("Input the second number - "))
# print("The total is", first_num+second_num)

# Задача 005. Предложите пользователюввести три числа. Сложитепервые два числа, 
# затем умножьте сумму на третье число. 
# Выведите результат в видеThe answer is [результат]
# first_num =int(input("Input the first number - "))
# second_num =int(input("Input the second number - "))
# third_num =int(input("Input the first number - "))
# print("The answer is", (first_num + second_num) * third_num )

# Задача 006. Спросите, сколько кусков пиццы было у пользователя и сколько кусков он съел.
# Вычислите, сколь-ко кусков пиццы у него осталось,
# и выведите результат в форме,удобной для пользователя
# print(int(input("Input how many slices of pizza did you have? ")) + int(input("Input how many slices do you have left? ")))

# Задача 007. Предложите пользователю ввести его имя и возраст. 
# Увеличьте возраст на 1 и выведите сообщение:
# [имя] next birthday you will be [новый возраст]
# name = input("What's your name? ")
# age = int(input("How old are you? "))
# print(name, "next birthday you will be", age+1)

# Задача 008. Предложите пользователю ввести общую сумму счета,
# а затем запросите общее количество участников обеда. 
# Разделите сумму счета на количество участникови выведите сумму, 
# которую должен заплатить каждый участник
# bill = int(input("What's the total cost of the bill? "))
# people = int(input("How many people are there? "))
# print("Each person should pay:", bill/people)

# Задача 009. Напишите программу, которая предлагает ввести промежуток времени в днях,
# а потом выводит количество часов, минут и секунд в этом промежутке
# day = int(input("Input the number of days - "))
# print("In", day, "days", day*24, "hours or", day*24*60, "minutes or", day*24*60*60, "seconds")

# Задача 010.В одном килограмме 2,204 фунта. Предложите пользователю ввести вес в кило-граммах 
# и переведите его в фунты
# weight = int(input("Input a number of kilos - "))
# print(round(weight*2.204,2), "pounds")

# Задача 011. Предложите пользователю ввести число больше 100, а затем число меньше 10.
# Сообщите, сколько раз меньшее число помещается в большем, в удобном формате.
# first_num = int(input("Input a number of 100 "))
# second_num = int(input("Input a number under 10 "))
# print(first_num//second_num)