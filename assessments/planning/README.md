<h1 align=center><strong>Toast Planning Homework</strong></h1>

This exercise lets you practice writing simple planning algorithms. The planning problem solved is a toy example for making a slice of toast.

Even if you do not do the tasks, it may be helpful for you to look at the file *planning/planning_problem.py* to understand how the planning problem from our learning unit can be implemented in Python.


# Setup
This project does not require additional dependencies beyond what's included in a standard Python installation.

# How to run?
You start the program by starting main.py
This script will compare all implemented planning functions based on different start states. The comparison will be based on:
- Whether or not the result is a correct goal state.
- How many states have been visited by the algorithm.
- How long the algoirthm ran
- How long making the toast took in the toasting world. This is represented by the attribute "time" within a state.


# Your Task

Your task is to implement the unimplemented functions in *planning/planner.py*
This file should contain different implementations of planning functions that will be compared. A random search algorthms is already implemented. Your task is to:
- Implement a breadth first search algorithm in function *breadth_first_search*
- Implement a custom algorithm in function *shortest_toast_time_search*. This algorithm should not only return a path to the goal but should return the shortest possible path, measured in time in the toasting world. This means the paramater ["time"] of the result should be minimized. If you want to challenge yourself you can also try to minimize the number of states this algorithm visits.

# Relation to Assessments

Solving this task can be used as basis for showing specific knowledge in Planning for an assessment in module *SE_14 Artificial Intelligence Basics*.