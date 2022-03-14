introString = "haha N O"
words = introString.split(",")
print(words)

def Greet(name):
    print("Hello, " + name + "! How are you?")
Greet("Constantin")

def CountWordsFromFile():
    FileName = input("Enter File Name: ")
    NumberOfWords = 0
    File = open(FileName, "r")
    for line in File:
        words = line.split()
        NumberOfWords = NumberOfWords + len(words)
    print("No. of Words: ")
    print(NumberOfWords)


CountWordsFromFile()