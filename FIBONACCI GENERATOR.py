def fibonacci_terms(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

if __name__ == "__main__":
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_sequence = fibonacci_terms(num_terms)
    print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
2
def fibonacci_max_value(max_value):
    fib_sequence = [0, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > max_value:
            break
        fib_sequence.append(next_value)
    return fib_sequence

if __name__ == "__main__":
    max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))
    fib_sequence = fibonacci_max_value(max_value)
    print(f"Fibonacci sequence up to {max_value}: {fib_sequence}")
