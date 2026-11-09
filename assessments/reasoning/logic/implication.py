
from logic.sentence import Sentence


class Implication(Sentence):
    """
        Implementation of implication
    """
    def __init__(self, antecedent, consequent):
        Sentence.validate(antecedent)
        Sentence.validate(consequent)
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (isinstance(other, Implication)
                and self.antecedent == other.antecedent
                and self.consequent == other.consequent)

    def __hash__(self):
        return hash(("implies", hash(self.antecedent), hash(self.consequent)))

    def __repr__(self):
        return f"Implication({self.antecedent}, {self.consequent})"

    def evaluate(self, model):
        return ((not self.antecedent.evaluate(model))
                or self.consequent.evaluate(model))

    def formula(self):
        antecedent = Sentence.parenthesize(self.antecedent.formula())
        consequent = Sentence.parenthesize(self.consequent.formula())
        return f"{antecedent} => {consequent}"

    def symbols(self):
        return set.union(self.antecedent.symbols(), self.consequent.symbols())

    def is_same(self,other):
        if type(other) == Implication:
            return self.antecedent(other.antecedent) and self.consequent(other.consequent)
        else:
            return False
