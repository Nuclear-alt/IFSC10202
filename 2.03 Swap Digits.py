number = int(input("Enter a Number"))
ones = number % 10
tens = number // 10
swapped = (ones * 10) + tens
print(f"Swapped Number: {swapped}")