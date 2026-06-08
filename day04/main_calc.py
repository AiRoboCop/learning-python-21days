import calculator

def main() -> None:
    a = 10
    b = 3

    print(f"a + b = {calculator.add(a, b)}")
    print(f"a - b = {calculator.subtract(a, b)}")
    print(f"a * b = {calculator.multiply(a, b)}")
    print(f"a / b = {calculator.divide(a, b):.2f}")

if __name__ == "__main__":
    main()