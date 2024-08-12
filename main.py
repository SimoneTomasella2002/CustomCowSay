import sys

# Functions

def getStringLines(userString) :
    lines = []
    maxLineLength = 50 if len(userString) >= 50 else len(userString) 

    numberOfLines = int(len(userString) / 50)

    # Getting n-1 lines
    for x in range(numberOfLines+1):
        line = userString[50*x:50*(x+1)]
        if (x == numberOfLines):
            lines.append(f"{line}{" " * (maxLineLength - len(line))}") # Last line
        else:
            lines.append(line)

    return lines

# Main flow functions

def checkArguments() :
    # Current version requres at least two arguments
    argumentValues = 2

    if (len(sys.argv) > argumentValues) :
        sys.stderr.write(f"You can't use more than {str(argumentValues)} arguments")
        sys.exit(-1)
    if (len(sys.argv) == 1) :
        sys.stderr.write("Write something in the CLI!")
        sys.exit(-1)


def printString() :
    userString = sys.argv[1]
    stringLength = len(str(userString))
    
    # Prints upper part of the balloon
    
    print("             /-", end='')
    
    if (stringLength < 10):     # If string is too short
        for _ in range(10):
            print("-", end='')
    else:
        if(stringLength < 50):
            for _ in range(stringLength):
                print("-", end='')
        else:
            for _ in range(50):
                print("-", end='')

    print("-\\")


    # Prints string content part of the balloon

    if (stringLength < 10):     # If string is too short
        print("             | " + userString, end='')
        for _ in range(10 - stringLength):
            print(" ", end='')
        print(" |")
    else:
        lines = getStringLines(userString)

        for line in lines:
            print(f"             | {line} |\n", end='')


    # Prints bottom part of the balloon

    print("             \\-", end='')

    if(stringLength < 10):      # If string is too short
        for _ in range(10):
            print("-", end='')
    else:
        if(stringLength < 50):
            for _ in range(stringLength):
                print("-", end='')
        else:
            for _ in range(50):
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


def main() :
    checkArguments()
    printString()
    printParrot()
    exit(0)
    
main()

# Parrot by Morfina on https://www.asciiart.eu/animals/birds-land