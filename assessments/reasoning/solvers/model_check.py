
"""
    Implementation of model checking algorithm.
"""

from logic.negation import Not


def check_all(knowledge, query, symbols, model):
        """Checks if knowledge base entails query, given a particular model."""

        # If model has an assignment for each symbol
        if not symbols:

            # If knowledge base is true in model, then query must also be true
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:

            # Choose one of the remaining unused symbols
            remaining = symbols.copy()
            p = remaining.pop()

            # Create a model where the symbol is true
            model_true = model.copy()
            model_true[p] = True

            # Create a model where the symbol is false
            model_false = model.copy()
            model_false[p] = False

            # Ensure entailment holds in both models
            return (check_all(knowledge, query, remaining, model_true) and
                    check_all(knowledge, query, remaining, model_false))


def model_check(knowledge, query):
    """
        parameters:
        - The knowledge base containing all knowledge. This is an And formula.
        - The query to check.

        returns:
        - True: if the query can be proven
        - False: if the query can be disproven
        - None: if the query can't be proven or disproven
    """
    
    # Get all symbols in both knowledge and query
    symbols = set.union(knowledge.symbols(), query.symbols())
    if check_all(knowledge, query, symbols, dict()):
         return True
    
    symbols = set.union(knowledge.symbols(), query.symbols())
    if check_all(knowledge, Not(query), symbols, dict()):
         return False
    
    return None


