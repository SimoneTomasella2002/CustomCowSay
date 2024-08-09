def checkArguments() :
    # Current version requres at least two arguments
    argumentValues = 2

    import sys
    if (len(sys.argv) > argumentValues) :
        sys.stderr.write("You can't use more than " + str(argumentValues) +  " arguments")
        sys.exit(-1)
    if (len(sys.argv) == 1) :
        sys.stderr.write("Write something in the CLI!")
        sys.exit(-1)


def printString() :
    import sys
    print(sys.argv[1])


def printParrot() :
    print("                           .");             
    print("                          | \\/|");
    print("  (\\   _                  ) )|/|");                     
    print("      (/            _----. /.'.'");
    print(".-._________..      .' @ _\\  .'");
    print("'.._______.   '.   /    (_| .')");
    print("  '._____.  /   '-/      | _.'");
    print("   '.______ (         ) ) \\ ");
    print("     '..____ '._       )  )");
    print("        .' __.--\\  , ,  // ((");
    print("        '.'     |  \\/   (_.'(");
    print("                '   \\ .'");
    print("                 \\   (");
    print("                  \\   '.");
    print("                   \\ \\ '.)");
    print("                    '-'-'");


def main() :
    checkArguments()
    printString()
    printParrot()
    
main()

# Parrot by Morfina on https://www.asciiart.eu/animals/birds-land