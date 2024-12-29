class Dictionary:
    def __init__(self):
        self.entries = {}

    def add_entry(self, word, meaning):
        self.entries[word.lower()] = meaning

    def search_word(self, word):
        word = word.lower()
        if word in self.entries:
            return self.entries[word]
        else:
            return "Word not found."

    def find_words_by_meaning(self, meaning):
        result = [word for word, m in self.entries.items() if m.lower() == meaning.lower()]
        if result:
            return result
        else:
            return "No words found with this meaning."

    def remove_entry(self, word):
        word = word.lower()
        if word in self.entries:
            del self.entries[word]
            return f"Word '{word}' removed."
        else:
            return "Word not found."

    def display_sorted_words(self):
        if self.entries:
            sorted_words = sorted(self.entries.keys())
            return "\n".join(sorted_words)
        else:
            return "No words in dictionary."

def main():
    dictionary = Dictionary()

    while True:
        print("\nDictionary Menu")
        print("1. Add a new entry")
        print("2. Search for a word")
        print("3. Find words with the same meaning")
        print("4. Remove a word")
        print("5. Display all words sorted alphabetically")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            word = input("Enter the word: ")
            meaning = input("Enter the meaning: ")
            dictionary.add_entry(word, meaning)
            print(f"Word '{word}' added to dictionary.")

        elif choice == '2':
            word = input("Enter the word to search: ")
            meaning = dictionary.search_word(word)
            print(f"Meaning of '{word}': {meaning}")

        elif choice == '3':
            meaning = input("Enter the meaning to search for: ")
            words = dictionary.find_words_by_meaning(meaning)
            if isinstance(words, list):
                print("Words with the given meaning:", ", ".join(words))
            else:
                print(words)

        elif choice == '4':
            word = input("Enter the word to remove: ")
            result = dictionary.remove_entry(word)
            print(result)

        elif choice == '5':
            print("Words sorted alphabetically:")
            print(dictionary.display_sorted_words())

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
