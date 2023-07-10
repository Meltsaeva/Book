# Задача 012。 Предложите пользователюввести два числа.
# Если первоечисло больше второго, сна-чала выведите второе число,а
# потом первое. В противномслучае выведите сначала пер-вое число, а потом второе
# first_num = int(input("Input the first number - "))
# second_num = int(input("Input the second number - "))
# if first_num > second_num:
#     print(second_num, first_num)
# elif first_num == second_num:
#     print("Incorrect")
# else:
#     print(first_num, second_num)

# Задача 013. Предложите пользовате-лю ввести число, меньшее20. 
# Если введенное числобольше или равно 20, выве-дите сообщение 
# «Too high»;в противном случае выведи-те сообщение «Thank you».
# num = int(input("Input a number less than 20 - "))
# if num >= 20:
#     print("Too high")
# else:
#     print("Thank you")

# Задача 014. Предложите пользователюввести число от 10 до 20 (вклю-чительно).
# Если будет введеночисло из этого диапазона, вы-ведите сообщение «Thank you»;
# в противном случае выведитесообщение «Incorrect answer»
# num = int(input("Input a number between 10 and 20 - "))
# if 10 <= num <= 20:
#     print("Thank you")
# else:
#     print("Incorrect answer")

# Задача 015. Предложите пользователю ввести любимый цвет. Если он введет «red», 
# «RED»или «Red», выведите сообщение «I like red too». 
# В противном случае выведите со-общение «I don’t like [colour], I prefer red»
# color = (input("Enter your favourite color - "))
# if str.lower(color) == "red":
#     print("I like red too")
# else:
#     print(f" I don't like {color} , I prefer red")

# Задача 016. Спросите пользователя, идет ли дождь. 
# Преобразуйте его ответ к нижнему регистру. 
# Если пользователь ответит «yes», спросите, ветрено ли на улице. 
# Если пользователь ответит «yes» и на второй вопрос, 
# выведите сообщение «It is too windyfor an umbrella»;
# в противном случае выведите сообщение «Take an umbrella».
# Если же пользователь не дал положительного ответа на первый вопрос, 
# выведите сообщение «Enjoy your day»
# rain = input("Is it raining? ")
# if str.lower(rain) == "yes":
#     wind = input("is it windy? ")
#     if str.lower(wind) == "yes":
#         print("It's too windy for an umbrella")
#     else:
#         print("Take an umbrella")
# else: 
#     print("Enjoy your day")

# Задача 017. Предложите пользователюввести его возраст. 
# Если введенное значение равно 18 и более, выведите сообщение 
# «You can vote»; если17 — сообщение «You canlearn to drive»;
# если 16 —сообщение «You can buy alottery ticket». 
# Если значениеменьше 16, выведите сообщение «You can go Trick-or-Treating»
# age = int(input("How old are you?"))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go Trick-or-Trating")

# Задача 018. Предложите пользователю ввести число. 
# Если оно меньше 10, вы-ведите сообщение «Too low»; 
# если число лежит в диапазоне от 10до 20 — сообщение «Correct». 
# В остальных случаях выведите со-общение «Too high
# num = int(input("Input a number - "))
# if num < 10:
#     print("Too low")
# elif 10 <= num <= 20:
#     print("Correct")
# else:
#     print("Too high")

# Задача 019. Предложите пользователю ввести значение 1, 2 или 3. 
# Если вве-дено значение 1, выведите сообщение «Thank you»; 
# если 2 — со-общение «Well done»; если 3 — сообщение «Correct». 
# Если введенолюбое другое значение, выведите сообщение «Error message»
# num = int(input("Input a number between 1 and 3  "))
# if num == 1:
#     print("Thank you")
# elif num == 2:
#     print("Well done")
# elif num == 3:
#     print("Correct")
# else:
#     print("Error message")

