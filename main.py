import sys

# Functions

def getStringLines(userString) :
    
    # New implementation
    lines = []
    leftPointer = 0
    rightPointer = 50 if len(userString) >= 50 else len(userString)-1
    firstLine = True

    while rightPointer < len(userString):
        
        #! Da riscrivere, bug con una sola linea
        if rightPointer >= 50:
            temp = rightPointer
            while userString[rightPointer] != ' ':
                rightPointer -= 1
                if rightPointer == leftPointer:
                    rightPointer = temp
                    break
        
        print(f"leftPointer = {leftPointer}, rightPointer = {rightPointer}")
        
        if(leftPointer == 0):
            lines.append(userString[leftPointer:rightPointer+1])
        else:
            lines.append(userString[leftPointer+1:rightPointer])

        leftPointer = rightPointer
        rightPointer = rightPointer + 50

        if rightPointer >= len(userString) and not firstLine:               # Last line check
            if (leftPointer == 0):                                          # If this is the first line
                lines.append(userString[leftPointer:len(userString)])
            else:
                lines.append(userString[leftPointer+1:len(userString)])     # A blankspace is in leftPointer, so we increment it by 1
            break

        firstLine = False
    
    return lines


    # Old implementation
    """
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
    """

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

    # New implementation
    userString = sys.argv[1]
    stringLength = len(str(userString))
    lines = getStringLines(userString)
    maxLineLength = 0
    
    for line in lines:
        if len(str(line)) > maxLineLength:
            maxLineLength = len(str(line))

    # Prints upper part of the balloon
    print("             /-", end='')

    if stringLength < 10:
        for _ in range(10):
            print("-", end='')
    else:
        for _ in range(maxLineLength):
            print("-", end='')
        
    print("-\\")


    # Prints content part of the balloon
    for line in lines:
        if maxLineLength < 10:
            print(f"             | {line}{" " * (10 - maxLineLength)} |")
        else:
            print(f"             | {line}{" " * (maxLineLength-len(str(line)))} |")


    # Prints bottom part of the balloon
    print("             \\-", end='')

    if stringLength < 10:
        for _ in range(10):
            print("-", end='')
    else:
        for _ in range(maxLineLength):
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