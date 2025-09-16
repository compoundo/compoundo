# Example: Guessing game
import random
def guessing_game():
	number = random.randint(1, 100)
	print("I'm thinking of a number between 1 and 100.")
	attempts = 0
	while True:
		guess = input("Take a guess: ")
		if not guess.isdigit():
			print("Please enter a valid number.")
			continue
		guess = int(guess)
		attempts += 1
		if guess < number:
			print("Too low!")
		elif guess > number:
			print("Too high!")
		else:
			print(f"Correct! You guessed it in {attempts} tries.")
			break


# Simple Python Program

def add_numbers():
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	result = num1 + num2
	print("The sum is:", result)
	if result > 10:
		print("That's a big number!")
	return result


# Example: Working with strings
def string_example():
	text = input("Enter a sentence: ")
	print("Uppercase:", text.upper())
	print("Lowercase:", text.lower())
	print("Number of characters:", len(text))
	print("First word:", text.split()[0] if text.split() else "(no words)")

# Example: Making choices with if/else
def if_else_example():
	age = int(input("Enter your age: "))
	if age < 18:
		print("You are a minor.")
	elif age < 65:
		print("You are an adult.")
	else:
		print("You are a senior.")

# Example: Reading and writing files
def file_example():
	filename = "example.txt"
	text = input("Type something to save to a file: ")
	with open(filename, "w") as f:
		f.write(text)
	print(f"Saved to {filename}.")
	print("Reading from file:")
	with open(filename, "r") as f:
		content = f.read()
		print(content)

def main():
	print("Choose an example to run:")
	print("1. Add numbers (loop, list)")
	print("2. Work with strings")
	print("3. If/else choices")
	print("4. Read/write files")
	print("5. Guessing game")
	choice = input("Enter 1, 2, 3, 4, or 5: ")
	if choice == "1":
		times = int(input("How many times do you want to add numbers? "))
		results = []
		for i in range(times):
			print(f"\nAddition #{i+1}")
			sum_result = add_numbers()
			results.append(sum_result)
		print("\nAll sums:")
		for idx, value in enumerate(results, 1):
			print(f"Addition #{idx}: {value}")
	elif choice == "2":
		string_example()
	elif choice == "3":
		if_else_example()
	elif choice == "4":
		file_example()
	elif choice == "5":
		guessing_game()
	else:
		print("Invalid choice.")

if __name__ == "__main__":
	main()
