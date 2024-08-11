import sys

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
    # Used in final line generation
    maxLineLength = 50 if stringLength >= 50 else stringLength 
    
    # Prints upper part of the balloon
    
    print("             /-", end='')
    
    if (stringLength < 10):     # If string is too short
        for(x) in range(10):
            print("-", end='')
    else:
        if(stringLength < 50):
            for x in range(stringLength):
                print("-", end='')
        else:
            for x in range(50):
                print("-", end='')

    print("-\\")


    # Prints string content part of the balloon

    if (stringLength < 10):     # If string is too short
        print("             | " + userString, end='')
        for(x) in range(10 - stringLength):
            print(" ", end='')
        print(" |")
    else:
        stringLines = int(len(userString) / 50)
        
        for x in range(stringLines+1):
            subString = userString[50*(x):50*(x+1)]
            if(x != stringLines):                               # All lines
                print(f"             | {subString} |\n", end='')
            else:                                               # Final line (covers also a single input line)
                print(f"             | {subString}", end='')
                for y in range(maxLineLength - len(subString)):
                    print(" ", end='')
                print(" |")
        

    # Prints bottom part of the balloon

    print("             \\-", end='')

    if(stringLength < 10):      # If string is too short
        for(x) in range(10):
            print("-", end='')
    else:
        if(stringLength < 50):
            for x in range(stringLength):
                print("-", end='')
        else:
            for x in range(50):
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