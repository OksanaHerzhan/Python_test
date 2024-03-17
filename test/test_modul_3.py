#Приклад_1_Для отримання поточної дати і часу використовується метод datetime.now():
#import datetime
#now = datetime.datetime.now()
#print(now)


# Приклад_2_ дата та час з модуля:
#from datetime import datetime
#
#current_datetime = datetime.now()
#
#print(current_datetime.year)
#print(current_datetime.month)
#print(current_datetime.day)
#print(current_datetime.hour)
#print(current_datetime.minute)
#print(current_datetime.second)
#print(current_datetime.microsecond)
#print(current_datetime.tzinfo)


# Приклад_3_В об'єкта datetime є методи, щоб отримати дату (без часу) та час (без дати):
#from datetime import datetime
#
#current_datetime = datetime.now()
#print(current_datetime.date())
#print(current_datetime.time())


# Приклад_4_Є зворотний метод datetime.combine який використовується для створення нового об'єкта datetime шляхом комбінування 
#об'єктів date та time. Це дозволяє створювати точний момент часу, вказуючи дату та час окремо, 
#а потім об'єднуючи їх
#
#import datetime
#
# Створення об'єктів date і time
#date_part = datetime.date(2023, 12, 14)
#time_part = datetime.time(12, 30, 15)
#
# Комбінування дати і часу в один об'єкт datetime
#combined_datetime = datetime.datetime.combine(date_part, time_part)
#
#print(combined_datetime) # Виведе "2023-12-14 12:30:15"


#Приклад_5_Щоб створити об'єкт datetime з конкретною вибраною датою у Python, можна використовувати 
#конструктор класу datetime.datetime, 
#передаючи йому рік, місяць, і день як аргументи
# час вказувати не обов'язково— якщо їх пропустити, вони будуть встановлені на 0

#import datetime
#
# Створення об'єкта datetime з конкретною датою
#specific_date = datetime.datetime(year=2020, month=1, day=7)
#
#print(specific_date)  # Виведе "2020-01-07 00:00:00"


# Приклад_6_Створення об'єкта datetime з датою та часом
#
#import datetime
#
# Створення об'єкта datetime з конкретною датою і часом
#specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)
#
#print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# Приклад_7_творення об'єкта datetime з датою та часом_інша візуалізація
#
#import datetime
#
# Створення об'єкта datetime з конкретною датою і часом
#specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)
#
#print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# Приклад_8_Метод weekday() використовується для отримання номера дня тижня для вказаної дати.
# Він повертає номер дня тижня, де понеділок має номер 0, а неділя - 6.
#
#from datetime import datetime

# Створення об'єкта datetime
#now = datetime.now()

# Отримання номера дня тижня
#day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
#print(f"Сьогодні: {day_of_week}")


# Приклад_9_порівняння двох об'єктів datetime

#from datetime import datetime

# Створення двох об'єктів datetime
#datetime1 = datetime(2023, 3, 14, 12, 0)
#datetime2 = datetime(2023, 3, 15, 12, 0)

# Порівняння дат
#print(datetime1 == datetime2)  # False, тому що дати не однакові
#print(datetime1 != datetime2)  # True, тому що дати різні
#print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
#print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2


# Приклад_10_клас timedelta, який використовується для представлення різниці між двома моментами в часі

#from datetime import timedelta
#delta = timedelta(
#    days=50,
#    seconds=27,
#    microseconds=10,
#    milliseconds=29000,
#    minutes=5,
#    hours=8,
#    weeks=2
#)
#print(delta)  # Результат 64 days, 8:05:56.000010


# Приклад_11_Якщо відняти від одного datetime об'єкту інший, то отримаємо timedelta об'єкт. 
# Він відповідає за відрізок часу між двома датами

#from datetime import datetime
#
#seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
#seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
#
#difference = seventh_day_2020 - seventh_day_2019
#print(difference)  # 365 days, 0:00:00
#print(difference.total_seconds())  # 31536000.0


# Приклад_12_Об'єкти timedelta можна створювати, щоб отримати дату/час віддалену від початкової дати
#
#from datetime import datetime, timedelta
#
#now = datetime.now()
#future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
#print(future_date)


# Приклад_13_Об'єкти timedelta можна створювати, щоб отримати дату/час віддалену від якоїсь конкретної дати
#
#from datetime import datetime, timedelta
#
#seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
#four_weeks_interval = timedelta(weeks=4)
#
#print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
#print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00


# Приклад_14_метод toordinal() - обчислення або порівняння, засновані на послідовності дат, 
# наприклад, для визначення кількості днів між двома датами
# повертає порядковий номер дня, враховуючи кількість днів з 1 січня року 1 нашої ери (тобто з початку християнського календаря)

#from datetime import datetime
#
# Створення об'єкта datetime
#date = datetime(year=2023, month=12, day=18)
#
# Отримання порядкового номера
#ordinal_number = date.toordinal()
#print(f"Порядковий номер дати {date} становить {ordinal_number}")


#Приклад_15_Наприклад ми хочемо визначити скільки пройшло повних днів, коли Наполеон спалив Москву, 
#а це відбулося 14 вересня 1812 року

#from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
#napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
#current_date = datetime.now()

# Розрахунок кількості днів
#days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
#print(days_since)


#Приклад_16_термін timestamp (часова мітка) використовується для вказівки конкретного моменту в часі
#Це зазвичай представляється як кількість секунд з певної початкової дати, найчастіше з 1 січня 1970 року в UTC
#timestamp є універсальним способом представлення часу, оскільки він не залежить від часових зон і календарних систем.
#перетворити об'єкт datetime в timestamp і навпаки. Конвертація datetime в timestamp
#
#from datetime import datetime
#
# Поточний час
#now = datetime.now()
#
# Конвертація datetime в timestamp
#timestamp = datetime.timestamp(now)
#print(timestamp)  # Виведе timestamp поточного часу


#Приклад_17_Конвертація timestamp в об'єкт datetime
#
#from datetime import datetime
#
# Припустимо, є timestamp
#timestamp = 1617183600
#
# Конвертація timestamp назад у datetime
#dt_object = datetime.fromtimestamp(timestamp)
#print(dt_object)  # Виведе відповідний datetime


# Приклад_18_метод strftime використовується для форматування об'єктів дати та часу datetime 
#у рядки за допомогою специфічних форматних кодів
# Цей метод дає можливість представити дату та час у зручному для читання форматі або в форматі, що відповідає специфічним вимогам

#from datetime import datetime
#
#now = datetime.now()
#
# Форматування дати і часу
#formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
#print(formatted_date) 
#
# Форматування лише дати
#formatted_date_only = now.strftime("%A, %d %B %Y")
#print(formatted_date_only)
#
# Форматування лише часу
#formatted_time_only = now.strftime("%I:%M %p")
#print(formatted_time_only)  
#
# Форматування лише дати
#formatted_date_only = now.strftime("%d.%m.%Y")
#print(formatted_date_only)


# Приклад_19_Метод strptime в Python використовується для перетворення рядків у об'єкти datetime. 
#Цей метод є протилежністю до strftime
#Розглянемо випадок коли з веб-сайту є рядок дата "2023.03.14" якогось посту 
#і нам треба перед тим як зберегти дату в базі даних перетворити її на об'єкт datetime
#
#from datetime import datetime
#
# Припустимо, у нас є дата у вигляді рядка
#date_string = "2023.03.14"
#
# Перетворення рядка в об'єкт datetime
#datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
#print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу


# Приклад_20_метод isoformat - Об'єкт datetime можна перетворити в рядок формату ISO 8601
#
#from datetime import datetime
#
# Поточна дата та час
#now = datetime.now()
#
# Конвертація у формат ISO 8601
#iso_format = now.isoformat()
#print(iso_format)


# Приклад_21_Для зворотного перетворення рядка у форматі ISO 8601 на об'єкт datetime, можна використати метод fromisoformat
#
#from datetime import datetime
#
#iso_date_string = "2023-03-14T12:39:29.992996"
#
# Конвертація з ISO формату
#date_from_iso = datetime.fromisoformat(iso_date_string)
#print(date_from_iso)


# Приклад_22_Метод isoweekday() у об'єкті datetime використовується для отримання дня тижня відповідно до ISO 8601
#
#from datetime import datetime
#
# Створення об'єкта datetime
#now = datetime.now()
#
# Використання isoweekday() для отримання дня тижня
#day_of_week = now.isoweekday()
#
#print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня


# Приклад_23_метод isocalendar(), який використовується для отримання кортежу, 
#що містить ISO рік, номер тижня в році та номер дня тижня відповідно до ISO 8601
#
#from datetime import datetime
#
# Створення об'єкта datetime
#now = datetime.now()
#
# Отримання ISO календаря
#iso_calendar = now.isocalendar()
#
#print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")


# Приклад_24_дата у форматі UTC - ЧЕРЕЗ додавання інформації про часову зону до об'єкта datetime
#from datetime import datetime, timezone
#
#local_now = datetime.now()
#utc_now = datetime.now(timezone.utc)
#
#print(local_now)
#print(utc_now)  # Виведе поточний час в UTC


# Приклад_25_Перетворення UTC часу в час, що відповідає Східному часовому поясу США (UTC-5 годин)
#from datetime import datetime, timezone, timedelta
#
#utc_time = datetime.now(timezone.utc)
#
# Створення часової зони для Східного часового поясу (UTC-5)
#eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
#print(eastern_time)  


# Приклад_26_
#from datetime import datetime, timezone, timedelta
#
# Припустимо, місцевий час належить до часової зони UTC+2
#local_timezone = timezone(timedelta(hours=2))
#local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)
#
# Конвертація локального часу в UTC
#utc_time = local_time.astimezone(timezone.utc)
#print(utc_time)  # Виведе час в UTC


#Приклад_27_Стандарт ISO 8601 також підтримує часові зони
#
#from datetime import datetime, timezone, timedelta
#
# Час у конкретній часовій зоні
#timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
#timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
#
# Конвертація у формат ISO 8601
#iso_format_with_timezone = timezone_datetime.isoformat()
#print(iso_format_with_timezone)


# Приклад_28_Модуль time - Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time)
#
#import time
#
#current_time = time.time()
#print(f"Поточний час: {current_time}")


#Приклад_29_Метод time.sleep(seconds) зупиняє виконання програми на вказану кількість секунд
#Наприклад цей код зупиняє виконання програми на 5 секунд
#
#import time
#
#print("Початок паузи")
#time.sleep(5)
#print("Кінець паузи")


# Приклад_30_Метод time.ctime([seconds]) перетворює часову мітку (кількість секунд) у зрозуміле для людини текстове представлення. 
#Якщо аргумент не вказаний, використовується поточний час
#
#import time
#
#current_time = time.time()
#print(f"Поточний час: {current_time}")
#
#readable_time = time.ctime(current_time)
#print(f"Читабельний час: {readable_time}")


# Приклад_31_Метод time.localtime([seconds]) перетворює часову мітку в структуру struct_time у місцевій часовій зоні
#
#import time
#
#current_time = time.time()
#print(f"Поточний час: {current_time}")
#
#local_time = time.localtime(current_time)
#print(f"Місцевий час: {local_time}")


# Приклад_32_використаємо time.perf_counter() для вимірювання часу виконання деякого блоку коду
#import time
#
# Записуємо час на початку виконання
#start_time = time.perf_counter()
#
# Виконуємо якусь операцію
#for _ in range(1_000_000):
#    pass  # Просто проходить цикл мільйон разів
#
# Записуємо час після виконання операції
#end_time = time.perf_counter()
#
# Розраховуємо та виводимо час виконання
#execution_time = end_time - start_time
#print(f"Час виконання: {execution_time} секунд")


# Приклад_33_представлення чисел з підкресленнями _ є способом зробити великі числа більш читабельними
#
# Один мільйон
#a = 1_000_000
#print(a)  # Виведе 1000000
#
# Десять мільйонів
#b = 10_000_000
#print(b)  # Виведе 10000000
#
# Один мільярд
#c = 1_000_000_000
#print(c)  # Виведе 1000000000


# Приклад_34_Робота з випадковими величинами_метод, наприклад, підходить для симуляції кидка кубика
#
#import random
#
#dice_roll = random.randint(1, 6)
#print(f"Ви кинули {dice_roll}")


# Приклад_35_  випадкове число в інтервалі 0, 1
#import random
#
#num = random.random()
#print(num)


# Приклад_36_ симулювати випадкове відсоткове заповнення
#
#import random
#
#fill_percentage = random.random() * 100
#print(f"Заповнення: {fill_percentage:.2f}%")


# Приклад_37_Метод random.randrange(start, stop[, step]) повертає випадково вибране число з заданого діапазону
#
#import random
#
#target = random.randrange(1, 11, 2)
#print(f"Ціль: {target}")

# Приклад_38_Коли у вас є список об'єктів і вам потрібно перемішати порядок елементів в цьому списку на випадковий, 
#ми використовуємо метод random.shuffle(x), 
#де x - список, який потрібно перемішати
# Перемішування колоди карт 
#
#import random
#
#cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
#
#random.shuffle(cards)
#
#print(f"Перемішана колода: {cards}")


# Приклад_39_Якщо потрібно вибрати випадковий елемент зі списку, нам потрібно використати метод random.choice(seq), 
#де seq - послідовність для вибору: список або кортеж.
#Вибір випадкового фрукта:
#
#import random
#
#fruits = ['apple', 'banana', 'orange']
#print(random.choice(fruits))


# Приклад_40_Простий вибір випадкового елемента зі списку
#
#import random
#
#items = ['яблуко', 'банан', 'вишня', 'диня']
#chosen_item = random.choices(items, k=1)
#rint(chosen_item)  


#Приклад_41_Вибір декількох елементів з можливістю повторень
#
#import random
#
#numbers = [1, 2, 3, 4, 5]
#chosen_numbers = random.choices(numbers, k=3)
#print(chosen_numbers)


#Приклад_42_Вибір з вагами
#
#import random
#
#colors = ['червоний', 'зелений', 'синій']
#weights = [10, 1, 1]
#chosen_color = random.choices(colors, weights, k=1)
#print(chosen_color)  


#Приклад_43_Створення випадкової команди з 4 учасників з групи з 10 осіб
#
#import random
#
#participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
#team = random.sample(participants, 4)
#print(f"Команда: {team}")


#Приклад_44_Приклад генерації випадкової ціни для продукту в межах від 50 до 100
#
#import random
#
#price = random.uniform(50, 100)
#print(f"Випадкова ціна: {price:.2f}")


#Приклад_45_робота з округленнями
#
#import math
#
# Вихідне число
#x = 3.7
#
# Використання різних методів округлення
#ceil_result = math.ceil(x)  # Округлення вгору
#floor_result = math.floor(x)  # Округлення вниз
#trunc_result = math.trunc(x)  # Відсікання дробової частини
#
#print(ceil_result, floor_result, trunc_result)


#Приклад_46_ використання пакета math
#
#import math
#
# Використання констант
#print(math.pi)  # Виведе приблизне значення π
#
# Тригонометрія
#angle = math.radians(60)  # Конвертація з градусів у радіани
#print(math.sin(angle))  # Синус кута
#
# Корінь числа
#print(math.sqrt(9))  # Квадратний корінь з 9
#
# Логарифми
#print(math.log(10, 2))  # Логарифм 10 за основою 2


#Приклад_47_Функція math.isclose використовується для порівняння двох чисел з певною допустимою похибкою.
#import math
#
#r = math.isclose(0.1 + 0.2, 0.3)
#print(r)  # Це поверне True


#Приклад_48_можемо виконувати порівняння з маленькою похибкою:
#
#import math
#
#r = math.isclose(0.1, 0.10000000009)
#print(r)  # Це поверне True

