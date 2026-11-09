
import random
from  planning.planning_problem import Planning_Problem 

class Planner():
    """
        Planner class with different planning method implementations
    """

    @classmethod
    def random_search(cls, start_state):
        """
            Implementation of random search.

            returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """

        open_list = [(start_state,[])] # this is a list of state,path. The path of the start state is empty.
        start_state["path"]  = [] # small hack: we add paths to the state in order to remember the path we travelled.
        step_count = 0
        
        while len(open_list) > 0:
            state, path = random.choice(open_list)
            step_count+= 1

            for action in Planning_Problem.actions:
                next_state = Planning_Problem.state_transition(state,action)
                next_path = path + [action]

                if Planning_Problem.goal(next_state):
                    return next_path, step_count
                else:
                    open_list.append((next_state,next_path))

        return None, step_count
    

    @classmethod
    def breadth_first_search(cls, start_state):
        """
            Implementation of Breadth First Search

            returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """
        step_count = 0
        
        # TODO: implement me

        return None, step_count
    

    @classmethod
    def shortest_toast_time_search(cls, start_state):
        """
            Implementation of a search algorithm that also optimized for the time it takes to toast a slice of bread.
            This time is measured within the state in attribute ["time"]

            returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """
        step_count = 0
        
        # TODO: implement me

        return None, step_count