# Задача 020. Предложите пользователю ввести имя. Выве-дите длину имени.
# print(len(input("What's your name? - ")))

# Задача 021.Предложите пользователю ввести сначала имя,а затем фамилию. 
# Соедините их, разделив пробелом, после чего выведите полное имя и его длину.
# firstname = input("What's your name? ")
# surname = input("What's your surname? ")
# name = firstname + " " + surname
# print(name, len(name) - 1)

# Задача 022.Предложите пользователю ввести имя и фамилию в нижнемрегистре. 
# Преобразуйте строки к титульному регистру и соедините их. Выведите полученный результат.
# firstname = input("What's your name? ")
# surname = input("What's your surname? ")
# name = firstname + " " + surname
# print(name.title())


# Задача 023. Предложите пользователюввести первую строку какого-нибудь стихотворения, выведите длину строки. 
# Запросите начальную и конечную позицию и выведите только эту часть строки 
# (не забудьте, чтов Python нумерация индексовначинается с 0, а не с 1).
# rhyme = input("Enter the first line of a nursery rhyme: ")
# print(len(rhyme))
# start = int(input("Enter a starting number - "))
# finish = int(input("Enter an end number - "))
# print(rhyme[start:finish])

# Задача 024. Предложите пользователю ввести имя. Выведите его в верхнем регистре.
# name = input("What's your name? ")
# print(name.upper())

# Задача 025. Предложите пользователю ввести имя. Если длина имени меньше 5 символов, 
# предложите ввести фамилию, соединитеих (без пробела) и выведите полное имя в верхнем 
# регистре.Если длина имени составляет 5 и более символов, выведите имя в нижнем регистре.
# name = input("What's your name? ")
# if len(name) <= 5:
#     surname =  input("What's your surname? ")
#     print(name.upper() + surname.upper())
# else:
#     print(name.lower())

# Задача 026. В шифре «поросячья латынь» начальная согласная буква слова перемещается в конец слова,
# и к ней добавляется суффикс «ay». Если слово начинается с гласной, к нему просто добавляется суффикс «way». 
# Например, pig превращается в igpay, banana — в ananabay,а aardvark — в aardvarkway. Напишите программу,которая 
# предлагает пользователю ввести слово и преобразует его в «поросячью латынь».
# Проследите за тем,чтобы новое слово выводилось в нижнем регистре.
word = input("Enter a word - ")
first = word[0]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    word_1 = word[1:len(word)] + first + "ay"
    print(word_1.lower())
else:
    print(word.lower() + "way")