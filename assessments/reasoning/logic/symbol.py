
from logic.sentence import Sentence


class Symbol(Sentence):
    """
        A logical symbol in propositional logic
    """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise Exception(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}
    
    def is_same(self,other):
        if type(other) == Symbol:
            return self.name == other.name
        else:
            return False
