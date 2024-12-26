strings = ["apple", "banana", "kiwi", "orange", "grape"]
string_length_tuples = [(s, len(s)) for s in strings]
sorted_tuples = sorted(string_length_tuples, key=lambda x: x[1])
print(sorted_tuples)
