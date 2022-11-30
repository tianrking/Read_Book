"""
File: wordwrap.py
Project 9.6

Copies words from one file to another, in such a manner that they
wrap within a given line width.  The line width and the input and
output file names are the inputs.  The line width should be no less
than 40 characters.
"""

from arraylist import ArrayList
from linkedlist import LinkedList

def main():
    # Take the input file name
    inName = input("Enter the input file name: ")
    # Take the output file name
    outName = input("Enter the output file name: ")
    # Take the line width
    lineWidth = int(input("Enter the line width: "))
    if lineWidth < 40:
        print("Error: line width must be >= 40 characters.")
    else:
        # Open the input file
        inputFile = open(inName, 'r')
        # Open the output file
        outputFile = open(outName, 'w')

        # Add words and newlines to the list
        lyst = LinkedList().listIterator()     # or use ArrayList here
        for line in inputFile:
            if line == "\n":
                lyst.insert("\n")
            else:
                words = line.split()
                for word in words:
                    lyst.insert(word)
        # Write the words to the output file, to fit within
        # line width
        lyst.first()
        currentWidth = 0
        while lyst.hasNext():
            word = lyst.next()
            if word == "\n":
                outputFile.write("\n\n")
                currentWidth = 0
            elif currentWidth + len(word) + 1 > lineWidth:
                outputFile.write("\n")
                lyst.previous()
                currentWidth = 0
            else:
                outputFile.write(word + " ")
                currentWidth += len(word) + 1
        outputFile.close()

if __name__ == "__main__":
    main()
