filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        text = file.read().lower()

    words = text.split()

    unique_words = set(words)

    print("Total Unique Words:", len(unique_words))

    print("\nUnique Words:")
    for word in sorted(unique_words):
        print(word)

except FileNotFoundError:
    print("File not found.")