
from logic.sentence import Sentence


class Not(Sentence):
    """
        a negation statement
    """
    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()
    

    def is_same(self,other):
        if type(other) == Not:
            return self.operand.is_same(other.operand)
        else:
            return False

