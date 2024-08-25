import sys
import os
MAX_LINE_LENGTH = 50
MIN_LINE_LENGTH = 10
MAX_ALLOWED_ARGUMENTS = 3

# Functions

def getStringLines(userString) :
    
    lines = []
    words = userString.split(" ")
    currentLine = []

    for word in words:
        # If currentLine + word exceeds MAX_LINE_LENGTH, then we append currentLine without new word
        # Second check is needed for edge cases like single words longer than MAX_LINE_LENGTH 
        if len(" ".join(currentLine) + word) > MAX_LINE_LENGTH and len(word) < MAX_LINE_LENGTH:
            lines.append(" ".join(currentLine))
            currentLine.clear()

        currentLine.append(word)

    # Last line
    lines.append(" ".join(currentLine))

    return lines


# Main flow functions

def checkArguments() :
    # Current version requres at least two arguments

    if (len(sys.argv) > MAX_ALLOWED_ARGUMENTS) :
        sys.stderr.write(f"You can't use more than {str(MAX_ALLOWED_ARGUMENTS)} arguments")
        sys.exit(-1)
    if (len(sys.argv) == 1) :
        sys.stderr.write("Write something in the CLI!")
        sys.exit(-1)
    if (len(sys.argv) == MAX_ALLOWED_ARGUMENTS) :
        if not os.path.exists(f"./customTxtFolder/{str(sys.argv[2])}"):
            sys.stderr.write("File does not exist!")
            sys.exit(-1)
    


def printString() :

    # New implementation
    userString = sys.argv[1]
    stringLength = len(str(userString))
    lines = getStringLines(userString)
    maxCurrentLineLength = 0
    
    for line in lines:
        if len(str(line)) > maxCurrentLineLength:
            maxCurrentLineLength = len(str(line))

    # Prints upper part of the balloon
    print("             /-", end='')

    if stringLength < MIN_LINE_LENGTH:
        for _ in range(MIN_LINE_LENGTH):
            print("-", end='')
    else:
        for _ in range(maxCurrentLineLength):
            print("-", end='')
        
    print("-\\")


    # Prints content part of the balloon
    for line in lines:
        if maxCurrentLineLength < MIN_LINE_LENGTH:
            print(f"             | {line}{" " * (MIN_LINE_LENGTH - maxCurrentLineLength)} |")
        else:
            print(f"             | {line}{" " * (maxCurrentLineLength-len(str(line)))} |")


    # Prints bottom part of the balloon
    print("             \\-", end='')

    if stringLength < MIN_LINE_LENGTH:
        for _ in range(MIN_LINE_LENGTH):
            print("-", end='')
    else:
        for _ in range(maxCurrentLineLength):
            print("-", end='')
        
    print("-/")


def printParrot() :
    print("                  \\  /     .")
    print("                   \\/     | \\/|")
    print("  (\\   _                  ) )|/|")
    print("      (/            _----. /.'.'")
    print(".-._________..      .' @ _\\  .'")
    print("'.._______.   '.   /    (_| .')")
    print("  '._____.  /   '-/      | _.'")
    print("   '.______ (         ) ) \\ ")
    print("     '..____ '._       )  )")
    print("        .' __.--\\  , ,  // ((")
    print("        '.'     |  \\/   (_.'(")
    print("                '   \\ .'")
    print("                 \\   (")
    print("                  \\   '.")
    print("                   \\ \\ '.)")
    print("                    '-'-'")


def printFromTxt(customTxt) :
    with open(f"./customTxtFolder/{customTxt}", "r") as file:
        print(file.read())


def main() :
    checkArguments()
    printString()
    
    printParrot() if(len(sys.argv) == 2) else printFromTxt(sys.argv[2])

    exit(0)
    
main()

# Parrot by Morfina on https://www.asciiart.eu/animals/birds-land
# Horse by Veronica Karlsson on https://www.asciiart.eu/animals/horses