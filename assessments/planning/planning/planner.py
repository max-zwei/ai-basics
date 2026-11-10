
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
        open_list = [(start_state,[])]
        visited_list = [[start_state["toaster_has_power"], 
                        start_state["toaster_is_on"], 
                        start_state["bread_location"], 
                        start_state["bread_state"]]] # to avoid looping through the same states
        
        # TODO: implement me
        # run all actions on start state, run all actions per first actions ... until goal reached
        # same list action as with homework: 
        # select the first node with list[0] to achieve breadth-first search

        while len(open_list) > 0:
            state, path = open_list[0]
            open_list.pop(0)
            step_count+= 1

            for action in Planning_Problem.actions:
                next_state = Planning_Problem.state_transition(state,action)
                next_path = path + [action]

                if Planning_Problem.goal(next_state):
                    return next_path, step_count
                else:
                    # only append if state wasnt visited yet, other times remain possible
                    possible_state = [next_state["toaster_has_power"], 
                                    next_state["toaster_is_on"], 
                                    next_state["bread_location"], 
                                    next_state["bread_state"]]
                    if possible_state not in visited_list:
                        open_list.append((next_state,next_path))
                        visited_list.append([next_state["toaster_has_power"], 
                                            next_state["toaster_is_on"], 
                                            next_state["bread_location"], 
                                            next_state["bread_state"]])

        return None, step_count
    

    @classmethod
    def shortest_toast_time_search(cls, start_state):
        """
            Implementation of a search algorithm that also optimized for the time it takes to toast a slice of bread.
            This time is measured within the state in attribute ["time"]

            returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """
        step_count = 0
        open_list = [(start_state,[])]
        visited_list = [start_state] # to avoid looping through the same states
        config_keys = ("toaster_has_power",
                       "toaster_is_on",
                       "bread_location",
                       "bread_state")
        
        # TODO: implement me
        # heuristic search but different
        # because I don't know a distance to goal but I know the paths I discovered and how much time they alread spent
        # So I always need to pick as next path the path with the least amount of time spent so far

        while len(open_list) > 0:
            # sort the open_list by state["time"]
            open_list.sort(key=lambda item: item[0]["time"])
                    
            # select the path with least time
            state, path = open_list.pop(0)
                    
            # check if the state has been reached with a quicker time already    
            state_config = tuple(state[key] for key in config_keys)
            best_time = None
            for visited_state in visited_list:
                visited_config = tuple(visited_state[key] for key in config_keys)
                if state_config == visited_config:
                    best_time = visited_state["time"]
                    break

            if best_time is not None and state["time"] > best_time:
                continue  # A cheaper route to this configuration is already known
                    
            # check if goal was reached
            if Planning_Problem.goal(state):
                return path, step_count
                    
            step_count+= 1

            # run the next actions
            for action in Planning_Problem.actions:
                next_state = Planning_Problem.state_transition(state,action)
                next_path = path + [action]

                next_config = tuple(next_state[key] for key in config_keys)
                found = False

                # check if the next state and path should be explored or not
                for i, visited_state in enumerate(visited_list):
                    visited_config = tuple(visited_state[key] for key in config_keys)
                            
                    # append the list if the same configuration with a lesser time was founde
                    if next_config == visited_config:
                        found = True
                        if next_state["time"] < visited_state["time"]:
                            visited_list[i] = next_state
                            open_list.append((next_state, next_path))
                            break
                            
                # append the list if a new configuration was found
                if not found:
                    visited_list.append(next_state)
                    open_list.append((next_state, next_path))
                        
        return None, step_count