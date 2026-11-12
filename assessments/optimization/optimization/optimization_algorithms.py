from itertools import product


from optimization.optimization_problem import Optimization_Problem


class Optimization_Algorithms():
    """
        Optimization class with different optimization method implementations
    """

    @classmethod
    def exhaustive_search(cls):
        """
            calculate the best values for toast and wait duration by searching all values exhaustively.
        """
        best_utility = float('-inf')
        best_solution = None

        for toast_duration in range(1,101):
            for wait_duration in range(1,101):
                for power_step in range(201):
                    utility = Optimization_Problem.utility(
                                toast_duration = toast_duration,
                                wait_duration = wait_duration,
                                power = power_step / 100.0)
                
                if utility > best_utility:
                    best_utility = utility
                    best_solution = (toast_duration,wait_duration,(power_step / 100.0))
        return best_solution, best_utility
    
    # 1) Implement hill-climbing for the parameters *toast_duration* and *wait_duration*
    # 2) Implement gradient-ascent for the parameters *toast_duration*,  *wait_duration* and *power*

    # tackled already as homework
    @classmethod
    def hill_climbing(cls):
        """
            calculate the best values for toast and wait duration by implementing Hill Climbing
        """

        def finding_next_climb(toast_duration, wait_duration):
            # Calculate the utility of the current position and its neighbours. 
            # 1 is the neighbor at +1, 0 at 0 and n1 at -1. 
            # The first index is for the toast_duration and the second index for the wait_duration.
            # Checking if the neighbor is withing the range of 1-100
            
            utility = Optimization_Problem.utility(toast_duration = toast_duration, wait_duration = wait_duration)

            if toast_duration < 100:
                utility_1_0 = Optimization_Problem.utility(toast_duration = (toast_duration + 1), wait_duration = wait_duration)
            else:
                utility_1_0 = 0
            if toast_duration > 1:
                utility_n1_0 = Optimization_Problem.utility(toast_duration = (toast_duration - 1), wait_duration = wait_duration)
            else:
                utility_n1_0 = 0
            if wait_duration > 1:
                utility_0_n1 = Optimization_Problem.utility(toast_duration = (toast_duration), wait_duration = (wait_duration - 1))  
            else:
                utility_0_n1 = 0
            if wait_duration < 100:
                utility_0_1 = Optimization_Problem.utility(toast_duration = (toast_duration), wait_duration = (wait_duration + 1))
            else:
                utility_0_1 = 0
            if toast_duration < 100 and wait_duration < 100:
                utility_1_1 = Optimization_Problem.utility(toast_duration = (toast_duration + 1), wait_duration = (wait_duration +1))
            else:
                utility_1_1 = 0
            if toast_duration > 1 and wait_duration > 1:
                utility_n1_n1 = Optimization_Problem.utility(toast_duration = (toast_duration - 1), wait_duration = (wait_duration - 1))                                  
            else:
                utility_n1_n1 = 0
            if toast_duration < 100 and wait_duration > 1:
                utility_1_n1 = Optimization_Problem.utility(toast_duration = (toast_duration + 1), wait_duration = (wait_duration - 1))
            else:
                utility_1_n1 = 0
            if toast_duration > 1 and wait_duration < 100:
                utility_n1_1 = Optimization_Problem.utility(toast_duration = (toast_duration - 1), wait_duration = (wait_duration +1))
            else:
                utility_n1_1 = 0

            neighbors = [[utility_1_0, toast_duration + 1, wait_duration], 
                         [utility_n1_0, toast_duration - 1, wait_duration],
                         [utility_0_n1, toast_duration, wait_duration -1],
                         [utility_0_1, toast_duration, wait_duration + 1],
                         [utility_1_1, toast_duration + 1, wait_duration + 1],
                         [utility_n1_n1, toast_duration - 1, wait_duration - 1],
                         [utility_1_n1, toast_duration + 1, wait_duration - 1],
                         [utility_n1_1, toast_duration - 1, wait_duration + 1]]

            # sort the utilities of the neighbors from max to min
            neighbors.sort(reverse=True)

            # check if the current utility is better or worse than its best neighbor. 
            # run the function again, if better neighbor was found.
            if utility > neighbors[0][0]:
                return (toast_duration, wait_duration), utility
            else:
                return finding_next_climb(neighbors[0][1], neighbors[0][2])

        # random starting point
        return finding_next_climb(50, 50)
                
    @classmethod
    def other_hill_climb(cls):
        """
            Calculate the best values for toast_duration, wait_duration and power.
            This will require a mixture of hill climbing and Gradient Ascent
        """
        # TODO: implement me
        # hill climbing:
        # Calculate the utility of the current position and its neighbours. 
        # 1 is the neighbor at +5, 0 at 0 and n1 at -5. 
        # The first index is for the toast_duration and the second index for the wait_duration.
        # Checking if the neighbor is withing the range of 1-100
        
        grid = 5
        
        # gradient ascend:
        # gradient = next_utility - current_utility
        # if the gradient is less than 1, the step is reduced from 5 to 1 with a linear scale
        
        def finding_next_climb(toast_duration, wait_duration):

            utility = Optimization_Problem.utility(toast_duration = toast_duration, wait_duration = wait_duration)

            # checking if neighbors are within range and calculating the valid neighbors
            if toast_duration < (101-grid):
                utility_1_0 = Optimization_Problem.utility(toast_duration = (toast_duration + grid), wait_duration = wait_duration)
            else:
                utility_1_0 = 0
            if toast_duration > grid:
                utility_n1_0 = Optimization_Problem.utility(toast_duration = (toast_duration - grid), wait_duration = wait_duration)
            else:
                utility_n1_0 = 0
            if wait_duration > grid:
                utility_0_n1 = Optimization_Problem.utility(toast_duration = (toast_duration), wait_duration = (wait_duration - grid))  
            else:
                utility_0_n1 = 0
            if wait_duration < (101 - grid):
                utility_0_1 = Optimization_Problem.utility(toast_duration = (toast_duration), wait_duration = (wait_duration + grid))
            else:
                utility_0_1 = 0
            if toast_duration < (101 - grid) and wait_duration < (101 - grid):
                utility_1_1 = Optimization_Problem.utility(toast_duration = (toast_duration + grid), wait_duration = (wait_duration + grid))
            else:
                utility_1_1 = 0
            if toast_duration > grid and wait_duration > grid:
                utility_n1_n1 = Optimization_Problem.utility(toast_duration = (toast_duration - grid), wait_duration = (wait_duration - grid))                                  
            else:
                utility_n1_n1 = 0
            if toast_duration < (101 - grid) and wait_duration > grid:
                utility_1_n1 = Optimization_Problem.utility(toast_duration = (toast_duration + grid), wait_duration = (wait_duration - grid))
            else:
                utility_1_n1 = 0
            if toast_duration > grid and wait_duration < (101 - grid):
                utility_n1_1 = Optimization_Problem.utility(toast_duration = (toast_duration - grid), wait_duration = (wait_duration + grid))
            else:
                utility_n1_1 = 0
            
            # listing the utilities and their direction: grid, 0, -grid
            neighbors = [[utility_1_0, grid, 0], 
                         [utility_n1_0, -grid, 0],
                         [utility_0_n1, 0, -grid],
                         [utility_0_1, 0, grid],
                         [utility_1_1, grid, grid],
                         [utility_n1_n1, -grid, -grid],
                         [utility_1_n1, grid, -grid],
                         [utility_n1_1, -grid, grid]]

            # sort the utilities of the neighbors from max to min
            neighbors.sort(reverse=True)

            # check if the current utility is better or worse than its best neighbor. 
            # run the function again, if better neighbor was found.
            if utility > neighbors[0][0]:
                return (toast_duration, wait_duration), utility
            else:
                # calculate gradient ascend (y2-y1/x)
                gradient_ascend = float((neighbors[0][0] - utility) / grid)
                if gradient_ascend < 1.0:
                    
                    step = int(grid * gradient_ascend)
                    if step == 0:
                        step = 1
                    
                    # initialise the durations with a default direction
                    next_toast_duration = toast_duration
                    next_wait_duration = wait_duration
                    
                    # add step to toast duration with the correct direction
                    if neighbors[0][1] == grid:
                        next_toast_duration = toast_duration + step
                    elif neighbors[0][1] == -grid:
                        next_toast_duration = toast_duration - step
                        
                    # add step to wait duration with the correct direction
                    if neighbors[0][2] == grid:
                        next_wait_duration = wait_duration + step
                    elif neighbors[0][2] == -grid:
                        next_wait_duration = wait_duration - step
                    
                    return finding_next_climb(next_toast_duration, 
                                              next_wait_duration)
                else:
                    return finding_next_climb(toast_duration + neighbors[0][1], 
                                              wait_duration + neighbors[0][2])

        # random starting point
        return finding_next_climb(50, 50)        
    

    @classmethod
    def gradient_ascent(cls):
        """
            Calculate the best values for toast_duration, wait_duration and power.
            This will require a mixture of hill climbing and Gradient Ascent
        """
        # TODO: implement me
        
        gradient_factor = 0.3
        gradient_factor_power = 0.01
        
        
        def finding_next_climb(toast_duration, wait_duration, power):
            
            # Calculate the utility of the current position
            utility = Optimization_Problem.utility(toast_duration = toast_duration, wait_duration = wait_duration, power = power)

            # create a list of neighbors
            # The first index is for the toast_duration, the second index for the wait_duration, the third for power
            # 1, 0, -1 is the direction of the neighbor value
            neighbors = [
                dict(zip(("wait duration", "toast duration", "power"), offsets))
                for offsets in product((-1, 0, 1), repeat=3)
                ]
            
            # Checking if the neighbor is withing the range of 1-100 for wait and toast duration
            # Checking if the power is within the range of 0-2 to use the same coarse level as the durations (100 steps)
            
            valid_neighbors = [
                neighbor for neighbor in neighbors
                # dropping the same position
                if not (neighbor["wait duration"] == 0 
                and neighbor["toast duration"] == 0
                and neighbor["power"] == 0)
                # dropping all positions outside the allowed range
                and 1 <= wait_duration + neighbor["wait duration"] <= 100
                and 1 <= toast_duration + neighbor["toast duration"] <= 100
                and 0.0 <= power + 0.02 * neighbor["power"] <= 2.0
                ]
            
            for neighbor in valid_neighbors:
                
                # Calculating the utility for each neighbor
                neighbor["utility"] = Optimization_Problem.utility(toast_duration = toast_duration + neighbor["toast duration"], 
                                                                   wait_duration = wait_duration + neighbor["wait duration"], 
                                                                   power = power + 0.02 * neighbor["power"])
                
                
                # gradient ascent for each neighbor:
                # Calculating the gradient of the neighbors
                # gradient = abs(utility - current_utility) / (sum of neighbors variables)
                
                if neighbor["toast duration"] != 0:
                    utility_toast = Optimization_Problem.utility(toast_duration = toast_duration + neighbor["toast duration"], 
                                                                   wait_duration = wait_duration, 
                                                                   power = power)
                    neighbor["gradient_toast"] = (utility_toast - utility) / (neighbor["toast duration"])
                else:
                    neighbor["gradient_toast"] = 0
                
                if neighbor["wait duration"] != 0:
                    utility_wait = Optimization_Problem.utility(toast_duration = toast_duration, 
                                                            wait_duration = wait_duration +  neighbor["wait duration"], 
                                                            power = power)
                    neighbor["gradient_wait"] = (utility_wait - utility) / (neighbor["wait duration"])
                else:
                    neighbor["gradient_wait"] = 0
                
                if neighbor["power"] != 0:
                    utility_power = Optimization_Problem.utility(toast_duration = toast_duration, 
                                                            wait_duration = wait_duration, 
                                                            power = power + 0.02 * neighbor["power"])
                    neighbor["gradient_power"] = (utility_power - utility) / (0.02 * neighbor["power"])
                else:
                    neighbor["gradient_power"] = 0
            
            
            # Re-validate the neighbors with the gradients
            valid_gradient_neighbors = [
                neighbor for neighbor in valid_neighbors
                # dropping all positions outside the allowed range
                if 1 <= int(wait_duration + gradient_factor * neighbor["gradient_wait"]) <= 100
                and 1 <= int(toast_duration + gradient_factor * neighbor["gradient_toast"]) <= 100
                and 0.0 <= power + gradient_factor_power * neighbor["gradient_power"] <= 2.0
                ]            
            
            for neighbor in valid_gradient_neighbors:
                
                # Calculating the utility for each neighbor
                neighbor["utility"] = Optimization_Problem.utility(toast_duration=int(toast_duration + gradient_factor * neighbor["gradient_toast"]),
                                                                    wait_duration=int(wait_duration + gradient_factor * neighbor["gradient_wait"]),
                                                                    power=float(power + gradient_factor_power * neighbor["gradient_power"]))
            
            # Sort for the best neighbor
            valid_gradient_neighbors.sort(key=lambda item: item["utility"], reverse=True)
            
            # Compare and either return current utility or re-run with best neighbor with a step based on gradient ascent
            if utility >= valid_gradient_neighbors[0]["utility"]:
                return (toast_duration, wait_duration, power), utility
            else:
                return finding_next_climb(toast_duration=int(toast_duration + gradient_factor * valid_gradient_neighbors[0]["gradient_toast"]),
                                          wait_duration=int(wait_duration + gradient_factor * valid_gradient_neighbors[0]["gradient_wait"]),
                                          power=float(power + gradient_factor_power * valid_gradient_neighbors[0]["gradient_power"]))

        # random starting point
        return finding_next_climb(50, 50, 1.0)  