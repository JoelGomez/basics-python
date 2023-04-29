"""
The pass statement is a statement that does nothing. 
It's just a placeholder for the code that you'll write 
in the future.
"""

counter = 1
top = 10
if counter <= top:
    counter += 1
else:
    pass


for i in range(1, 6):
    if i % 2 == 0:
        pass
    else:
        print(f'{i} its odd')
    
for i in range(5):
    pass