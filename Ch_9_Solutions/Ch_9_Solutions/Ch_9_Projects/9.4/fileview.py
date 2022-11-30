"""
File: fileview.py
Project 9.4

View for a file viewer.  Supports navigation
through the lines of a file.

"""

from filemodel import FileModel

class FileView(object):

    def __init__(self):
        self._getFile()
        self._methods = {}          # Jump table for commands
        self._methods["1"] = self._first
        self._methods["2"] = self._next
        self._methods["3"] = self._previous
        self._methods["4"] = self._last
        self._methods["5"] = self._getFile
        self._methods["6"] = self._quit

    def run(self):
        """A menu-driven command processor for a user."""
        while True:
            print("1  Move to first line")
            print("2  Move to next line")
            print("3  Move to previous line")
            print("4  Move to last line")
            print("5  View a new file")
            print("6  Quit\n")
            number = input("Enter a number: ")
            theMethod = self._methods.get(number, None)
            if theMethod is None:
                print("Unrecognized number")
            else:
                theMethod()
                if self._model is None:
                    break

    def _getFile(self):
        filename = input("Enter a file name: ")
        self._model = FileModel(filename)
        line = self._model.first()
        self._printLine(line)

    def _first(self):
        line = self._model.first()
        self._printLine(line)

    def _last(self):
        line = self._model.last()
        self._printLine(line)

    def _next(self):
        line = self._model.next()
        self._printLine(line)

    def _previous(self):
        line = self._model.previous()
        self._printLine(line)

    def _printLine(self, line):
        if line is None:
            print("No line available")
        else:
            print(line)
            
    def _quit(self):
        self._model = None
        print("Have a nice day!")


# Launch the application
if __name__ == "__main__":
    FileView().run()
