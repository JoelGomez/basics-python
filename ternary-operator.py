"""
Ternary Operator

"""
age = 18

if age < 18:
    ticket_price = 5
else:
    ticket_price = 15

# To make it more concise, you can use an alternative syntax like this:

ticket_price = 5 if age < 18 else 15

# this is the structure
# value_if_true if condition else value_if_false


price = 50

if price <=50 :
    print('ta barato')
else:
    print('ta caro')

print ('ta barato') if price <= 50 else print('ta caro')


num_toys = 10

if num_toys > 20:
    print('tienes muchos juguetes')
else:
    print('esta decente')


print ('tienes muchos juguetes') if num_toys > 20 else print ('esta decente')


print(True) if age >=18 else print(False)