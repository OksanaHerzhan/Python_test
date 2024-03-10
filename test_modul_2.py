# num = 15  # приклад значення для num

# if num > 10:
 #   print("num більше за 10")
# else:
 #   print("num не більше за 10")


#a = 7
#if a > 0:
 #   print ('Число додатнє')
#elif a < 0:
 #   print ("число від'ємне")
#else:
 #   print ("це число - нуль")


#money = 0
#if money:
 #   print(f"You have {money} on your bank account")
#else:
 #   print("You have no money and no debts")


#result = None
#if result:
#    print(result)
#else:
#    print("Result is None, do something")

#user_name = input("Enter your name: ")
#if user_name:
#    print(f"Hello {user_name}")
#else:
#    print("Hi Anonym!")


#a = [1, 2, 3]
#b = a
#c = [1, 2, 3]

#print(a is b)  # True
#print(a is c)  # False


#name = "Taras"
#age = 22
#has_driver_licence = True

#if name and age >= 18 and has_driver_licence:
#    print(f"User {name} can rent a car")


#num = int(input("Ведіть число: "))
#lenght = len(str(num))
#if lenght == 2 and num % 2 == 0:
#    print ("Парне двозначне число")
#else:
#    print ("Ні")


#num = int(input())
#if num % 3 == 0 and num % 5 == 0:
#    print ('FizzBuzz')
#elif num % 3 == 0:
#    print ('Fizz')
#elif num % 5 == 0:
#    print ('Buzz')
#else:
#    print (num)


#x = int(input('x: '))
#y = int(input('y: '))

#if x >= 0:
#    if y >= 0:  # x > 0, y > 0
#        print("Перша чверть")
#    else:  # x > 0, y < 0
#        print("Четверта чверть")
#else:
#    if y >= 0:  # x < 0, y > 0
#        print("Друга чверть")
#    else:  # x < 0, y < 0
#        print("Третя чверть")


#fruit = "apple"

#match fruit:
#   case "apple":
#        print("This is an apple.")
#    case "banana":
#        print("This is a banana.")
#    case "orange":
#        print("This is an orange.")
#    case _:
#        print("Unknown fruit.")


#point = (1, 0)

#match point:
#    case (0, 0):
#        print("Точка в центрі координат")  
#    case (0, y):
#        print(f"Точка лежить на осі Y: y={y}")  
#    case (x, 0):
#        print(f"Точка лежить на осі X: x={x}") 
#    case (x, y):
#        print(f"Точка має координати:  x={x}, y={y}") 
#    case _:
#        print("Це не точка")


#pets = ["dog", "cat", "fish"]

#match pets:
#    case ["dog", "cat", _]:
#        # Випадок, коли є і собака, і кіт
#        print("There's a dog and a cat.")
#    case ["dog", _, _]:
#        # Випадок, коли є тільки собака
#        print("There's a dog.")
#    case _:
#        # Випадок для інших комбінацій
#        print("No dogs.")


#fruit = 'apple'
#for char in fruit:
#    print(char)


#alphabet = "abcdefghijklmnopqrstuvwxyz"
#for char in alphabet:
#    print(char, end=" ")


#some_iterable = ["a", "b", "c"]
#
#for i in some_iterable:
#    print(i)


#odd_numbers = [1, 3, 5, 7, 9]
#for i in odd_numbers:
#    print(i ** 2)


# Зчитування рядка від користувача:
#user_input = input("Введіть рядок: ")

# Ініціалізація змінних для підрахунку символів та пробілів:
#total_chars = len(user_input)  # загальна кількість символів у рядку
#space_count = 0  # кількість пробілів

# Підрахунок кількості пробілів:
#for char in user_input:
#    if char == " ":
#        space_count += 1

# Виведення результатів:
#print(f"Загальна кількість символів у рядку: {total_chars}")
#print(f"Кількість пробілів у рядку: {space_count}")


#k = 0
#while k < 10:
#    k = k + 1
#print(k)


#a = 0
#while True:
#    print(a)
#    if a >= 20:
#        break
#    a = a + 1


#a = 0
#while a < 6:
#    a = a + 1
#    if not a % 2:
#        continue
#print (a)


#a = 0
#while True:
#    print(a)
#    if a >= 20:
#        break
#    a = a + 1



#a = 0
#while a < 6:
#    a = a + 1
#    if not a % 2:
#        continue
#    print(a)


# приклад використовує цикл for разом з range для ітерації через послідовність чисел
# Функція range створює послідовність чисел
#for i in range(5):
#    print(i)


# Ітерація з визначеним початком і кінцем ітерації. Приклад виведення чисел від 2 до 9
#for i in range(2, 10):
#    print(i)


# Ітерація з кроком. Цей приклад виведе парні числа від 0 до 8
#for i in range(0, 10, 2):
#    print(i)


# функція enumerate(some_list) створює пари індекс-значення для кожного елемента в списку, і цикл for проходить по цих парах.
#some_list = ["apple", "banana", "cherry"]
#for index, value in enumerate(some_list):
#    print(index, value)


# У цьому випадку zip(list1, list2) об'єднує елементи з list1 та list2, і цикл for проходить по створеним словосполученням
#list1 = ["зелене", "стигла", "червоний"]
#list2 = ["яблуко", "вишня", "томат"]
#for number, letter in zip(list1, list2):
#    print(number, letter)


# У цьому прикладі list1 має 3 елементи, тоді як list2 має 5 елементів. Оскільки list1 є коротшим, zip припинить ітерацію після третьої пари значень

#list1 = [1, 2, 3]
#list2 = ['a', 'b', 'c', 'd', 'e']

#for number, letter in zip(list1, list2):
#    print(number, letter)


#numbers = {
#    1: "one",
#    2: "two",
#    3: "three"
#}
# Ітеруючи за словником, ви перебираєте ключі словника
#for key in numbers:
#    print(key)

#for key in numbers.keys():
#    print(key)

# перебрати саме значення словника, для цього скористаємося методом values
#for val in numbers.values():
#    print(val)

# щоб перебрати пари ключ значення словника треба використати метод items
#for key, value in numbers.items():
#    print(key, value)


#val = 'a'
#try:
#    val = int(val)
#except ValueError:
#    print(f"val {val} is not a number")
#else:
#    print(val > 0)
#finally:
#    print("This will be printed anyway")


#age = input("How old are you? ")
#try:
#    age = int(age)
#    if age >= 18:
#        print("You are adult.")
#    else:
#        print("You are infant")
#except ValueError:
#    print(f"{age} is not a number")

#def say_hello():
		# тіло функції
#    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
#say_hello()

# ще один виклик функції
#say_hello()


#def print_max(a, b):
#    if a > b:
#        print(a, 'максимально')
#    elif a == b:
#        print(a, 'дорівнює', b)
#    else:
#        print(b, 'максимально')
#
#print_max(3, 4)  # пряма передача значень
#
#x = 5
#y = 7
#print_max(x, y)  # передача змінних у якості аргументів


#def print_max(a: int, b: int):
#    if a > b:
#        print(a, 'максимально')
#    elif a == b:
#        print(a, 'дорівнює', b)
#    else:
#        print(b, 'максимально')
#
#print_max(3, 4)  # пряма передача значень
#
#x = 5
#y = 7
#print_max(x, y)  # передача змінних у якості аргументів


#def add_numbers(num1: int, num2: int) -> int:
#    sum = num1 + num2
#    return sum
#
#result = add_numbers(5, 10)
#print(result)  # Виведе: 15


#def greet(name: str) -> str:
#    return f"Привіт, {name}!"
#
#greeting = greet("Олексій")
#print(greeting)  # Виведе: Привіт, Олексій!


#def is_even(num: int) -> bool:
#    return num % 2 == 0
#
#check_even = is_even(4)
#print(check_even)  # Виведе: True


#def modify_string(original: str) -> str:
#    original = "змінено"
#    return original
#
#str_var = "оригінал"
#print(modify_string(str_var))  # виведе: змінено
#print(str_var)                # виведе: оригінал


#def modify_list(lst: list) -> None:
#    lst.append(4)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3, 4]


#def modify_list(lst: list) -> None:
#    lst = lst.copy()
#    lst.append(4)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3]


#def string_to_codes(string: str) -> dict:
#    # Ініціалізація словника для зберігання кодів
#    codes = {}  
#    # Перебір кожного символу в рядку
#    for ch in string:  
#        # Перевірка, чи символ вже є в словнику
#        if ch not in codes:
#            # Додавання пари символ-код в словник  
#            codes[ch] = ord(ch)  
#    return codes
#result = string_to_codes("Hello world!")
#print(result)


#x = 50
#
#def func() -> None:
#    x = 2
#    print('Зміна локального x на', x)  # Зміна локального x на 2
#
#func()
#print('Глобальний x як і раніше', x)  # x як і раніше 50


#def outer_func():
#    enclosing_var = "Я змінна в функції, що охоплює"
#
#    def inner_func():
#        print("Всередині вкладеної функції:", enclosing_var)
#
#    inner_func()
#
#outer_func()


#x = 50
#
#def func():
#    global x
#    print('x дорівнює', x)  # x дорівнює 50
#    x = 2
#    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2
#
#func()
#print('Значення x складає', x)# Значення x складає 2


#def say_hello():
		# тіло функції
#    print('Привіт, Світ!')

# Кінець функції say_hello()

# виклик функції
#say_hello()

# ще один виклик функції
#say_hello()


#def print_max(a, b):
#    if a > b:
#        print(a, 'максимально')
#    elif a == b:
#        print(a, 'дорівнює', b)
#    else:
#        print(b, 'максимально')

#print_max(3, 4)  # пряма передача значень

#x = 5
#y = 7
#print_max(x, y)  # передача змінних у якості аргументів


#def print_max(a: int, b: int):
#    if a > b:
#        print(a, 'максимально')
#    elif a == b:
#        print(a, 'дорівнює', b)
#    else:
#        print(b, 'максимально')
#
#print_max(3, 4)  # пряма передача значень
#
#x = 5
#y = 7
#print_max(x, y)  # передача змінних у якості аргументів


#def add_numbers(num1: int, num2: int) -> int:
#    sum = num1 + num2
#    return sum
#
#result = add_numbers(5, 10)
#print(result)  # Виведе: 15


#def greet(name: str) -> str:
#    return f"Привіт, {name}!"
#
#greeting = greet("Олексій")
#print(greeting)  # Виведе: Привіт, Олексій!


#def is_even(num: int) -> bool:
#    return num % 2 == 0
#
#check_even = is_even(4)
#print(check_even)  # Виведе: True


#def modify_string(original: str) -> str:
#    original = "змінено"
#    return original
#
#str_var = "оригінал"
#print(modify_string(str_var))  # виведе: змінено
#print(str_var)                # виведе: оригінал


#def modify_list(lst: list) -> None:
#    lst.append(4)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3, 4]


#def modify_list(lst: list) -> None:
#    lst = lst.copy()
#    lst.append(4)
#
#my_list = [1, 2, 3]
#modify_list(my_list)
#print(my_list)  # виведе: [1, 2, 3]


#def string_to_codes(string: str) -> dict:
    # Ініціалізація словника для зберігання кодів
#    codes = {}  
    # Перебір кожного символу в рядку
#    for ch in string:  
        # Перевірка, чи символ вже є в словнику
#        if ch not in codes:
            # Додавання пари символ-код в словник  
#            codes[ch] = ord(ch)  
#    return codes
#result = string_to_codes("Hello world!")
#print(result)


#x = 50
#
#def func() -> None:
#    x = 2
#    print('Зміна локального x на', x)  # Зміна локального x на 2
#
#func()
#print('Глобальний x як і раніше', x)  # x як і раніше 50


#def outer_func():
#    enclosing_var = "Я змінна в функції, що охоплює"
#
#    def inner_func():
#        print("Всередині вкладеної функції:", enclosing_var)
#
#    inner_func()
#
#outer_func()


#def func_outer():
#    x = 2
#
#    def func_inner():
#        nonlocal x
#        x = 5
#
#    func_inner()
#    return x
#
#result = func_outer()  # 5
#print(result)


#x = 50
#
#def func():
#    global x
#    print('x дорівнює', x)  # x дорівнює 50
#    x = 2
#    print('Змінюємо глобальне значення x на', x)  # Змінюємо глобальне значення x на 2
#
#func()
#print('Значення x складає', x)# Значення x складає 2


#def greet(name, message="Привіт"):
#    print(f"{message}, {name}!")
#    # використовує значення за замовчуванням для message
#greet("Олексій")  
#
## передача власного значення для message
#greet("Марія", message="Добрий день") 


#def func(a, b=5, c=10):
#    print('a дорівнює', a,', b дорівнює', b,', а c дорівнює', c)
#
## a дорівнює 3, b дорівнює 7, а c дорівнює 10
#func(3, 7)
#
## a дорівнює 25, b дорівнює 5, а c дорівнює 24
#func(25, c=24)
#
## a дорівнює 100, b дорівнює 5, а c дорівнює 50
#func(c=50, a=100)


#def say(message, times=1):
#    print(message * times)
#
#say('Привіт') 
#say('Світ', 5)


#def real_cost(base: int, discount: int = 0) -> int:
#    return base * (1 - discount)
#price_bread = 15
#price_butter = 50
#price_sugar = 60
#
#current_price_bread = real_cost(price_bread)
#current_price_butter = real_cost(price_butter, 0.05)
#current_price_sugar = real_cost(price_sugar, 0.07)
#
#print(f'Нова вартість хліба: {current_price_bread}')
#print(f'Нова вартість масла: {current_price_butter}')
#print(f'Нова вартість цукру: {current_price_sugar}')


#def print_all_args(*args):
#    for arg in args:
#        print(arg)
#
#print_all_args(1, 'hello', True)


#def concatenate(*args) -> str:
#    result = ""
#    for arg in args:
#        result += arg
#    return result
#
#print(concatenate("Hello", " ", "world", "!"))


#def concatenate(*strings) -> str:
#    result = ""
#    for arg in strings:
#        result += arg
#    return result
#
#print(concatenate("Hello", " ", "world", "!"))


#def greet(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")
#
#greet(name="Alice", age=25)


#def example_function(*args, **kwargs):
#    print("Позиційні аргументи:", args)
#    print("Ключові аргументи:", kwargs)
#
#example_function(1, 2, 3, name="Alice", age=25)


#def greet(name, age):
#    print(f"Hello {name}, you are {age} years old.")
#
#person_info = {"name": "Alice", "age": 25}
#greet(**person_info)


#def factorial(n):
#    if n == 0: # базовий випадок
#        return 1
#    else:
#        return n * factorial(n-1) # рекурсивний випадок
#
#print(factorial(5)) # виведе 120


#def fibonacci(n):
#    if n <= 1: # базовий випадок
#        return n
#    else:
#        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок
#
#print(fibonacci(10)) # виведе 55


#def factorial(n):
#    print("Виклик функції factorial з n = ", n)
#    if n == 1:
#        print("Базовий випадок, n = 1, повернення 1")
#        return 1
#    else:
#        result = n * factorial(n-1)
#        print("Повернення результату для n = ", n, ": ", result)
#        return result
#
#print(factorial(5))


#result = None
#if result:
#    print(result)
#else:
#    print("Result is None, do something")
#
#user_name = input("Enter your name: ")
#if user_name:
#    print(f"Hello {user_name}")
#else:
#    print("Hi Anonym!")


#num = int(input("Enter a number: "))
#if num > 0 :
#    if num % 2 == 1:
#        result = "Positive odd number"
#        print(result)
#    else:
#        result = "Positive even number"
#        print(result)
#elif num < 0:
#    result = "Negative number"
#    print(result)
#else:
#    result = "It is zero"
#    print(result)


#def format_string(string, length):
#    if len(string) >= length:
#        return string
#    else:
#        spaces = (length - len(string)) // 2
#        formatted_string = " " * spaces + string
#        return formatted_string


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    number_new = factorial(n) / (factorial (n - k) * factorial(k))
    return number_new

n = int(50)
k = int(7)

resalt = number_of_groups(n, k)
