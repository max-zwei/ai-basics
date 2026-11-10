
from planning.planner import Planner
from  planning.planning_problem import Planning_Problem 
import time

def test_planner(planner_name, planning_function, start_state):
    """
        Tests one specific planning function and prints out the test results.
    """

    print("\nTesting " + planner_name)

    start = time.time_ns()
    plan, step_count = planning_function(start_state)
    end = time.time_ns()
    time_ns = end - start


    if plan is None:
        print("- not implemented")
    else:
        # apply plan to start state to check
        state = start_state
        for action in plan:
            state = Planning_Problem.state_transition(state,action)

        print("- result:", plan)
        print("- correct plan:", Planning_Problem.goal(state))
        print("- states visited:",step_count)
        print("- execution time:",time_ns, "ns")
        print("- toasting world time:", state["time"])




# this is a test function. It tests your plan function 
def test_all(start_state):
    """
        tests all planning functions
    """
    print("\n\n testing:",start_state)

    test_planner("Random Search", Planner.random_search, start_state)
    test_planner("Breadth First Search", Planner.breadth_first_search, start_state)
    test_planner("Shortest Toast Time Search", Planner.shortest_toast_time_search, start_state)

if __name__ == "__main__":
    # execute the test for a few test cases
    test_all(Planning_Problem.example_state)
    test_all({'toaster_has_power': True, 'toaster_is_on': False, 'bread_location': 'toaster', 'bread_state': 'untoasted', 'time': 0})
    test_all({'toaster_has_power': True, 'toaster_is_on': True, 'bread_location': 'plate', 'bread_state': 'untoasted', 'time': 0})
    test_all({'toaster_has_power': False, 'toaster_is_on': True, 'bread_location': 'plate', 'bread_state': 'untoasted', 'time': 0})