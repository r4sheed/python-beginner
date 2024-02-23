import time
import random

# 2024.02.21.

# List of animal names
animal_names = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'fox', 'wolf', 'rabbit', 'deer']

# https://docs.python.org/3/library/functions.html#open
# Meaning
# 'r'
# open for reading (default)

# 'w'
# open for writing, truncating the file first

# 'x'
# open for exclusive creation, failing if the file already exists

# 'a'
# open for writing, appending to the end of file if it exists

# 'b'
# binary mode

# 't'
# text mode (default)

# '+'
# open for updating (reading and writing)

# Open the file using 'with' to ensure it's closed properly
with open('message.txt', 'w') as fileHandle:
    for index in range(0, 10):
        value = random.randint(0, 100)
        animal = random.choice(animal_names)

        # F-string használata: Az f-string használatával egyszerűbb és olvashatóbb a szöveg formázása.
        text = f'Number: {value}, Animal: {animal}'
        fileHandle.write(text + '\n')

        # A {} kapcsos zárójelek közé helyezett változók neveit a f-strings (f'' vagy f"") segítségével helyettesíthetjük be a szövegbe. Az f a string előtti karakter megjelölése, ami a függőleges vonal (|) mellett az angol QWERTY-billentyűzeten található. Az így formázott stringek lehetővé teszik a változók vagy kifejezések közvetlenül a stringbe való beágyazását. A példában a text változót helyettesítjük be a stringbe.
        print(f'Writing \'{text}\' to file')

        time.sleep(0.5)

# Az if __name__ == '__main__': kifejezés a Pythonban használt szokásos módszer, amely lehetővé teszi azt, hogy a kód egyes részei csak akkor futnak le, ha a fájlt közvetlenül futtatod, és nem importálod egy másik Python fájlból. Amikor egy Python fájlt importálsz egy másik fájlba, akkor a __name__ változó értéke az importált fájl neve lesz. Ha a fájlt közvetlenül futtatod, akkor a __name__ változó értéke '__main__'.
if __name__ == '__main__':

    # print(animal_names[0])  # Kiírja a 'cat' nevű állatot, mivel az első elem a listában
    # print(animal_names[animal_names.index('cat')])  # Kiírja a 'cat' nevű állatot, ha isméd a listában lévő indexet
            
    # Egyedi állatok kiírása:
    print('Unique animals:')
    unique_animals = set(animal_names)
    for animal in unique_animals:
        print(animal)

    # Különböző állatok száma:
    unique_animals = set(animal_names)
    print(f"There are {len(unique_animals)} unique animals.")

    # Véletlenszerű állat kiírása:
    random_animal = random.choice(animal_names)
    print(f"Random animal: {random_animal}")

    # Állatok száma:
    print(f"There are {len(animal_names)} animals in the list.")

    # Állatok listázása:
    print("\n".join(animal_names))