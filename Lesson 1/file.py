import time
import random

# List of animal names
animal_names = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'fox', 'wolf', 'rabbit', 'deer']

# https://docs.python.org/3/library/functions.html#open
# Meaning
# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - open for exclusive creation, failing if the file already exists
# 'a' - open for writing, appending to the end of file if it exists
# 'b' - binary mode
# 't' - text mode (default)
# '+' - open for updating (reading and writing)

# Open the file using 'with' to ensure it's closed properly
with open('message.txt', 'w') as fileHandle:
    for index in range(0,  10):
        value = random.randint(0,  100)
        animal = random.choice(animal_names)

        # Using f-string for easier and more readable text formatting.
        text = f'Number: {value}, Animal: {animal}'
        fileHandle.write(text + '\n')

        # The variables placed inside the curly braces {} in the f-string (f'' or f"") can be replaced in the text using f-strings. The 'f' character before the string indicates this, allowing for the direct embedding of variables or expressions into the string. The formatted strings enable the direct embedding of variables or expressions into the string. In this example, the 'text' variable is replaced in the string.
        print(f'Writing \'{text}\' to file')

        time.sleep(0.5)

# The 'if __name__ == '__main__':' expression is a common practice in Python, which allows certain parts of the code to run only when the file is run directly, and not imported from another Python file. When a Python file is imported from another file, the value of the '__name__' variable is the name of the imported file. When the file is run directly, the value of the '__name__' variable is '__main__'.
if __name__ == '__main__':

    # Print the 'cat' animal, as it is the first element in the list
    # Print the 'cat' animal if you know the index in the list
             
    # Printing unique animals:
    print('Unique animals:')
    unique_animals = set(animal_names)
    for animal in unique_animals:
        print(animal)

    # Number of different animals:
    unique_animals = set(animal_names)
    print(f"There are {len(unique_animals)} unique animals.")

    # Printing a random animal:
    random_animal = random.choice(animal_names)
    print(f"Random animal: {random_animal}")

    # Number of animals:
    print(f"There are {len(animal_names)} animals in the list.")

    # Listing animals:
    print("\n".join(animal_names))