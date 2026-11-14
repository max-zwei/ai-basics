
from copy import deepcopy
from logic.biconditional import Biconditional
from logic.implication import Implication
from logic.negation import Not


def is_in(knowledge, query):
    for conjunct in knowledge.conjuncts:
        if conjunct.is_same(query):
            return True
    return False

def check_proven(knowledge, query):
    """
        checks whether the query is currently proven or disproven in the knowledge base.

        returns:
        - True: if the query is contained
        - False: if the negation of the query is contained.
        - None: else
    """
    if is_in(knowledge,query):
        return True
    elif is_in(knowledge,Not(query)):
        return False
    else:
        None

def get_inferrable_knowledge(knowledge):
    """
        Takes a knowledge base and finds all sentences that can be inferred.

        returns a list of sentences that can be inferred from the knowlede base.
    """
    inferrable_knowledge = []
    for sentence in knowledge.conjuncts:
        if type(sentence) is Implication:
            if is_in(knowledge,sentence.antecedent) and not is_in(knowledge,sentence.consequent):
                inferrable_knowledge.append(sentence.consequent)
        if type(sentence) is Biconditional:
            left_known = is_in(knowledge,sentence.left)
            right_known = is_in(knowledge, sentence.right)

            if left_known and not right_known:
                inferrable_knowledge.append(sentence.right)
            elif right_known and not left_known:
                inferrable_knowledge.append(sentence.left)
    return inferrable_knowledge

            


def forward_search(knowledge, query):
    """
        solved the query by doing forward search.
    
        parameters:
        - The knowledge base containing all knowledge. This is an And formula.
        - The query to check. This is expected to be a symbol.

        returns:
        - True: if the query can be proven
        - False: if the query can be disproven
        - None: if the query can't be proven or disproven
    """

    # Best practice: copy the knowledge base so we don't accidentally modify an input parameter.
    knowledge_base = deepcopy(knowledge)

    # TODO: implement me
    
    # use check_proven to check knowledge against the query, return the result of check_proven if it is True or False
    # if return None, use get_inferrable_knowledge to find new conclusions
    
    while check_proven(knowledge_base, query) == None:
        
        new_knowledge = get_inferrable_knowledge(knowledge_base)
        
        if len(new_knowledge) > 0:
            
            # add new conclusions to knowledge_base and run again
            for news in new_knowledge:
                knowledge_base.add(news)
        
        else:
            
            # if nothing can be inferred the query is unresolved, return None
            return None
        
    return check_proven(knowledge_base, query)
