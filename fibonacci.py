import os

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(b)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        user_input = input("Enter how many Fibonacci numbers to generate: ")
        num = int(user_input)

        if num <= 0:
            print("Please enter a positive integer.")
        else:
            result = fibonacci(num)
            print("Fibonacci sequence:")
            print(result)

            filename = f"fibonacci_output_{num}.txt"
            with open(filename, "w") as file:
                file.write("Fibonacci sequence:\n")
                file.write(", ".join(map(str, result)))

            print(f"Saved to {filename}")
        print(f"Writing to: {filename} in {os.getcwd()}")



    except ValueError:
        print("Invalid input. Please enter a whole number like 10 — not '10.txt' or letters.")
