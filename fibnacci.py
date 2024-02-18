def fibonacci(n):
fib_sequence = [0, 1]
while len(fib_sequence) < n:
fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
return fib_sequence
num_terms = int(input("Enter the number of Fibonacci numbers to generate: "))
result = fibonacci(num_terms)
print(f"Fibonacci sequence of {num_terms} terms: {result}")
