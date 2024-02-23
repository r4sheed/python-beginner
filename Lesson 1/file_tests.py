import unittest
import random

# List of animal names
animal_names = ['cat', 'dog', 'elephant', 'lion', 'tiger', 'bear', 'fox', 'wolf', 'rabbit', 'deer']

class TestAnimalNames(unittest.TestCase):

    def test_all_animals(self):
        # Test that all animals are in the list
        self.assertEqual(len(animal_names),  10)
        self.assertIn('cat', animal_names)
        self.assertIn('dog', animal_names)
        self.assertIn('elephant', animal_names)
        # ... add more animals as needed

    def test_unique_animals(self):
        # Test that all animals are unique
        unique_animals = set(animal_names)
        self.assertEqual(len(unique_animals), len(animal_names))

    def test_random_animal(self):
        # Test that a random animal is chosen from the list
        random_animal = random.choice(animal_names)
        self.assertIn(random_animal, animal_names)

    def test_animal_count(self):
        # Test that the count of animals is correct
        self.assertEqual(len(animal_names),  10)

    def test_animal_listing(self):
        # Test that the animals are listed correctly
        animal_listing = "\n".join(animal_names)
        self.assertIsInstance(animal_listing, str)
        self.assertEqual(len(animal_listing.split('\n')), len(animal_names))

    def test_animal_by_number(self):
        # Test that animals are listed by a specific number
        for animal in animal_names:
            if animal == 'cat':
                self.assertIn(animal, animal_names)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()