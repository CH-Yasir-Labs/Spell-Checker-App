#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     05/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)

            # Ensure corrected_word is not None and different from the original
            if corrected_word and corrected_word.lower() != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}'")
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)  # Keep the original if no correction

        return ' '.join(corrected_words)

    def run(self):
        print("\n--- Spell Checker ---")

        while True:
            text = input("Enter text to check (or type 'exit' to quit): ")

            if text.lower() == "exit":
                print("Closing Program.")
                break

            corrected_text = self.correct_text(text)  # Fixed method call
            print(f"Corrected Text: {corrected_text}")

if __name__ == '__main__':
    SpellCheckerApp().run()

