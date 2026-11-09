"""
    This is the main file of this exercise. It calls the model checker and forward search algorithms on different problems and compares their performance.
"""



import time

from logic.conjunction import And
from logic.disjunction import Or
from logic.implication import Implication
from logic.negation import Not
from logic.symbol import Symbol
from solvers.forward_search import forward_search
from solvers.model_check import model_check


def test_problem(problem_name, knowledge, query):
    """
        Tests one specific planning function and prints out the test results.
    """

    print("\nTesting " + problem_name)

    print("... running model checking")
    start_model_check = time.time_ns()
    result_model_check = model_check(knowledge, query)
    end_model_check = time.time_ns()
    time_model_check_ns = end_model_check - start_model_check

    print("... running forward search")
    start_forward_search = time.time_ns()
    result_forward_search = forward_search(knowledge, query)
    end_forward_search = time.time_ns()
    time_forward_search_ns = end_forward_search - start_forward_search
    
    print("... done. \n")

    print("- result - model checking: ", result_model_check)
    print("- result - forward search: ", result_forward_search)
    print("- time for model checking", time_model_check_ns, "ns")
    print("- time for forward search", time_forward_search_ns, "ns")





# this is a main function. It tests different reasoning problems and prints comparison between model checking and forward search
def main():
    """
        tests all planning functions
    """

    A = Symbol("A")
    B = Symbol("B")
    C = Symbol("C")
    D = Symbol("D")
    E = Symbol("E")
    F = Symbol("F")
    G = Symbol("G")
    H = Symbol("H")
    I = Symbol("I")
    J = Symbol("J")
    K = Symbol("K")
    L = Symbol("L")
    M = Symbol("M")
    N = Symbol("N")
    O = Symbol("O")

    knowledge_1 = And(A,
                      Implication(A,B),
                      Implication(B, And(B, Not(C))),
                      Implication(And(B,Not(C)),D),
                      Implication(D,E),
                      Implication(E,F))
    test_problem("Problem 1", knowledge=knowledge_1, query=F)


    knowledge_2 = And(A, G, H, I, J, K, L, M, N, O,
                      Implication(B, And(B, Not(C))),
                      Implication(A,B),
                      Implication(And(B,Not(C)),D),
                      Implication(D,E),
                      Implication(E,F))
    test_problem("Problem 2", knowledge=knowledge_2, query=F)


    knowledge_3 = And(A,
                      Implication(B, And(B, Not(C))),
                      Implication(A,B),
                      Implication(And(B,Not(C)),D),
                      Implication(D,E),
                      Implication(E,Not(F)))
    test_problem("Problem 3", knowledge=knowledge_3, query=F)

    knowledge_4 = And(A,
                      Implication(B, And(B, Not(C))),
                      Implication(A,B),
                      Implication(And(B,Not(C)),D),
                      Implication(D,E),
                      Implication(E,Not(F)))
    test_problem("Problem 4", knowledge=knowledge_4, query=G)

    knowledge_5 = And(A,
                      Not(B),
                      Implication(A,Or(B, C)))
    test_problem("Problem 5", knowledge=knowledge_5, query=C)

if __name__ == "__main__":
    main()




