import os
class RuinedNikuldenDinnerError(Exception):
    """Custom exception for file reading errors in validate_recipe."""
    pass

def validate_recipe(filename):
    """Validate if a recipe contains specific words."""
    target_words = ['риба', 'рибена', 'шаран', 'сьонга']
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the file content and convert to lowercase
            content = file.read().lower()
            # Check if any target word is in the content
            return any(word in content for word in target_words)
    except (OSError, IOError):
        # Raise the custom exception if there's an error reading the file
        raise RuinedNikuldenDinnerError("Failed to read the recipe file")

print(validate_recipe('Challenges/test.txt'))