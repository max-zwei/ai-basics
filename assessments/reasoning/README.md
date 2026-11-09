<h1 align=center><strong>Forward Search Homework</strong></h1>

In this exercise you will implement a Forward Search algorithm and compare it against model checking.


# Credit:
The implementation of propositional logic is to a large extent based on the content of the course CS50: Introduction to Computer Science (https://pll.harvard.edu/course/cs50-introduction-computer-science) 


# Setup
This project does not require additional dependencies beyond what's included in a standard Python installation.

# How to run?
You start the program by starting main.py
The script does not require additional arguments.

# Your Task

Your task is to implement the method *forward_search* in *solvers/forward_search.py*. This method should implement a forward search algorithm. It takes two arguments:
- knowledge: the knowledge base. This is an And-connected formula that describes all you know to be true. 
- query: the query you want to proof.

The algorithm should return ...
- True if the query can be proven from the knowledge
- False if Not(query) can be provem fron the knowledge
- None else.


For this implementation, the following convenience methods have already been implemented:
- check_proven checks whether the query is currently already proven in the current state of the knowledge base.
- get_inferrable_knowledge takes the knowledge base and returns a list of all logical sentences that can be inferred. Inference is done by looking at all Implication and Biconditional statements within the knowledge base.

The script *main.py* compares your algoirthm against the model checker from the knights and knaves task (slightly adapted to fit the task specification here). It compares the result and the run time based on a number of different problems.

A few tips:
- Test Problem 2 is more complex than the others. It's a good case study to get an impression of the time complexity of your algorithm compared to model checking. Your algorithm should be a lot faster than model checking on this test case. Do you understand why?
- Your algorithm should have the same result as model checking in Test Problem 1 to 4.
- Your algorithm will likely not be able to solve Test Problem 5 (meaning it will return None rather than the correct result). Can you find out why? 

# Relation to Assessments

Solving this task can be used as basis for showing specific knowledge in Reasoning for an assessment in module *SE_14 Artificial Intelligence Basics*.