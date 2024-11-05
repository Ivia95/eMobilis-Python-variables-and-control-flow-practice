class Calculator:
    count = 0  # Static attribute to track the number of calls to add()

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

# Using the static method and updating the count
result1 = Calculator.add(3, 5)
print(f"Result of first addition: {result1}")
print(f"Add method called: {Calculator.count} times")

result2 = Calculator.add(10, 20)
print(f"Result of second addition: {result2}")
print(f"Add method called: {Calculator.count} times")

result3 = Calculator.add(7, 8)
print(f"Result of third addition: {result3}")
print(f"Add method called: {Calculator.count} times")
