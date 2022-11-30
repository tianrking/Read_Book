"""
File: expressiontree.py
Project 10.7  Completes the node classes for expression trees.

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    def __init__(self, data):
        self.data = data

    def value(self):
        return self.data
      
    def __str__(self):
        return str(self.data)

    def prefix(self):
        return str(self)

    def infix(self):
        return str(self)

    def postfix(self):
        return str(self)

class InteriorNode(object):
    """Represents an operator and its two operands."""

    def __init__(self, op, leftOper, rightOper):
        self.operator = op
        self.leftOperand = leftOper
        self.rightOperand = rightOper

    def value(self):
        value1 = self.leftOperand.value()
        value2 = self.rightOperand.value()
        return self.computeValue(self.operator, value1, value2)

    def prefix(self):
        return str(self.operator) + " " + \
               self.leftOperand.prefix() + " " + \
               self.rightOperand.prefix()

    def infix(self):
        return "(" + self.leftOperand.infix() + " " + \
               str(self.operator) + " " + \
               self.rightOperand.infix() + ")"
    
    def postfix(self):
        return self.leftOperand.postfix() + " " + \
               self.rightOperand.postfix() + " " + \
               str(self.operator)

    def computeValue(self, op, value1, value2):
        """Utility routine to compute a value."""
        result = 0
        theType = op.getType()
        if theType == Token.PLUS:
            result = value1 + value2
        elif theType == Token.MINUS:
            result = value1 - value2
        elif theType == Token.MUL:
            result = value1 * value2
        elif theType == Token.DIV:
            if value2 == 0:
                raise ZeroDivisionError("Attempt to divide by 0")
            else:
                result = value1 // value2
        return result


def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3) - (2 + 3)):", c.infix())
    print("Expect - * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -       :", c.postfix())
    print("Expect 15                      :", c.value())

if __name__ == "__main__":
    main()




