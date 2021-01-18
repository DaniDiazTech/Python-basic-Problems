def minion_game(string):
    string = string.upper()
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    print(*[f"Stuart {stuart}" if stuart >
            kevin else f"Kevin {kevin}" if kevin > stuart else "Draw"])

if __name__ == '__main__':
    s = input()
    minion_game(s)
