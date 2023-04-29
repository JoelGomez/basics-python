"""
if statement 
You use the if statement to execute a block of code based on a specified condition.
"""

age = 18
if age >= 18:
    print("Mayor de edad")

# If the condition evaluates to True, it executes the statements in the if-block.
# Otherwise, it ignores the statements.

"""
if-else statement
Typically, you want to perform an action when a condition is True and 
another action when the condition is False.
To do so, you use the if...else statement.
"""

salary = 38_000

if salary >= 38_000:
    print("Menos del 10 % de población en México tiene un salario como este")
else:
    print("El salario promedio de un Mexicano ronda los 8,000 mxp ")

# In this syntax, the if...else will execute the if-block if the condition evaluates to True. 
# Otherwise, it’ll execute the else-block.
"""
Python if…elif…else statement
If you want to check multiple conditions and perform an action accordingly, 
you can use the if...elif...else statement. The elif stands for else if.
"""

age = 25
if age <=11:
    print("Eres un niño")
elif age >=12 and age <=18:
    print("eres un joven")
elif age >= 19 and age <= 26:
    print("ya eres un adulto")
else:
    print("ya se te esta llendo el tren")