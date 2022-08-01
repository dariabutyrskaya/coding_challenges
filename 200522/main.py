# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

def upped():
    processed_string = []

    while True:
        try:
            s = input()
# when we recieve EOF from the user (ctrl d) -> break
        except EOFError:
            break
#uppend the uppercased string
        processed_string.append(s.upper())

    for i in processed_string:
        print(i)
