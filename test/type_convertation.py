#num_1 = str(1)
#num_2 = int(float(str(1.8)))
#string_1 = int('3')
#print(type(num_1), type(num_2), type(string_1))

volume = float(input('Fuel volume: '))
price = float(input('Fuel price: '))
bill = f'Your bill {volume * price} uah'
print(bill)
print(type(volume), type(price))