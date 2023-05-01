"""

"""

def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(100, 0.1)
print(net_price)

net_price = get_net_price(price = 100, discount=0.1)
print(net_price)


def circle_diameter(circunference):
    diameter = circunference / 3.141516
    return diameter

print(circle_diameter(circunference = 10))

def multiplication(multiplicand = 2, multiplier = 5):
    return multiplicand * multiplier

print(multiplication()) #10
print(multiplication(10, 5)) #50
print(multiplication(multiplicand=8))#40
print(multiplication(multiplier=3))# 6
print(multiplication(multiplicand=9,multiplier=9))#81
