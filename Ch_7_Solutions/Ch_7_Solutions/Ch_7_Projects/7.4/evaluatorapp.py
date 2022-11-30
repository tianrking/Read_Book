"""
File: evaluatorapp.py
Project 7.3
View for the postfix expression evaluator.
Handles user interaction.
"""

from model import PFEvaluatorModel

class PFEvaluatorView(object):

    def run(self):
        evaluator = PFEvaluatorModel()
        while True:
            sourceStr = input("Enter a postfix expression: ")
            if sourceStr == "": break
            try:
                print(evaluator.format(sourceStr))
                print(evaluator.evaluate(sourceStr))
            except Exception as e:
                print(e, evaluator.evaluationStatus())

PFEvaluatorView().run()
