"""
File: parsers.py
Project 10.9

Defines Parser
"""

from tokens import Token
from scanner import Scanner
from expressiontree import LeafNode, InteriorNode

class Parser(object):

    def parse(self, sourceStr):
        self.completionMessage = "No errors"
        self.parseSuccessful = True
        self.scanner = Scanner(sourceStr)
        tree = self.expression()
        self.accept(self.scanner.get(), Token.EOE,
                     "symbol after end of expression")
        return tree
   
    def parseStatus(self):
        return self.completionMessage
    
    def accept(self, token, expected, errorMessage):
        if token.getType() != expected:
            self.fatalError(token, errorMessage)

    def fatalError(self, token, errorMessage):
        self.parseSuccessful = False
        self.completionMessage = "Parsing error -- " + \
                                  errorMessage + \
                                  "\nExpression so far = " + \
                                  self.scanner.stringUpToCurrentToken()
        raise Exception(self.completionMessage)

    def expression(self):
        tree = self.term()
        token = self.scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            self.scanner.next()
            tree = InteriorNode(token, tree, self.term())
            token = self.scanner.get()
        return tree

    def term(self):
        tree = self.factor()
        token = self.scanner.get()
        while token.getType() in (Token.MUL, Token.DIV):
            self.scanner.next()
            tree = InteriorNode(token, tree, self.factor())
            token = self.scanner.get()
        return tree

    def factor(self):
        tree = self.primary()
        token = self.scanner.get()
        if token.getType() == Token.EXPO:
            self.scanner.next()
            tree = InteriorNode(token, tree, self.factor())
            token = self.scanner.get()
        return tree

    def primary(self):
        token = self.scanner.get()
        if token.getType() == Token.INT:
            tree = LeafNode(token.getValue())
            self.scanner.next()
        elif token.getType() == Token.L_PAR:
            self.scanner.next()
            tree = self.expression()
            self.accept(self._scanner.get(),
                         Token.R_PAR,
                         "')' expected")
            self.scanner.next()
        else:
            tree = None
            self.fatalError(token, "bad primary")
        return tree

