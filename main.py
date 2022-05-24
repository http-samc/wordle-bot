# Initialize the word list
with open("words.txt", "r") as f:
    words = f.readlines()

data = {
    "known": [None] * 5,
    "exists": [None] * 5,
    "dne": []
}

def guess(data: dict, num: int):
    if num == 1:
        print("Gusess 1: CRANE")
        return "crane"

    possibleGuesses = []
    for word in words:

        # Check containing all known characters (know letter & position)
        missingKnownChar = False

        # Check doesn't contain any unknown characters (unknown letter)
        hasUnknownChar = False

        # Check that an existing character isn't repeated in a new guess
        duplicatesExisitngCharPos = False

        # Check containing all existing characters (know letter)
        realExistingChars = []
        for char in data["exists"]:
            if char:
                realExistingChars.append(char)

        # Iterate over all characters
        for i in range(5):
            char = word[i]
            if len(data["known"]) < i + 1:
                print(i, data["known"])

            if data["known"][i] and char != data["known"][i]:
                missingKnownChar = True
                break
            if char in data["dne"]:
                hasUnknownChar = True
                break
            if char == data["exists"][i]:
                duplicatesExisitngCharPos = True
                break
            if char in realExistingChars:
                realExistingChars.remove(char)

        # Skip if word doesn't meet criteria
        if (missingKnownChar
            or hasUnknownChar
            or duplicatesExisitngCharPos
            or realExistingChars
        ):
            continue

        # Add word to possible guesses
        possibleGuesses.append(word)

    # print(f'Gusess {num + 1}: {possibleGuesses[0]}')
    return possibleGuesses[0]

# Starting script
lastGuess = "crane"

guess(data, 1)

for u in range(5):
    # Get wordle response
    for pos in range(5):
        char = lastGuess[pos]
        charType = input("Type (0*: DNE, 1: E, 2: K): ")
        if charType == "":
            charType = 0
        charType = int(charType)
        if charType == 0 and char not in data["dne"]:
            data["dne"].append(char)
        elif charType == 1:
            data["exists"][pos] = char
        elif charType == 2 and char not in data["known"]:
            data["known"][pos] = char
        for i, char in enumerate(data["exists"]):
            if char in data["known"]:
                data["exists"][i] = None

    lastGuess = guess(data, u + 2)
    print(data)
    print(f'Guess {u+2}: {lastGuess}')