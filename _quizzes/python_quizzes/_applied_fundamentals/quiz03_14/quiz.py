x =[1,2,3]
y = x
y.append(4)
print(x)

def mystery_function(x, y=10):
    return x + y

check = mystery_function(y=5,x=10)

print(check)