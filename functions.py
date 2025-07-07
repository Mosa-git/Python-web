
def greet(name):
    print(f"Hello, {name}")

def add(a, b):
    return a + b

greet("Mosa")

result = add(2, 5)
print(result)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
    def greet(name, greeting="Hello"):
        print(f"{greeting}, {name}")
        
    greet("Mosa", "Good morning")