

class Planning_Problem():
    """
        This class represents the planning problem
    """

    actions=(
            "plug_in_toaster", # will connect the toaster to the socket, if it isn't already connected. Otherwise does nothing
            "unplug_toaster", # will disconnect the toaster from the socket. If toaster is on, it switches to off automatically.
            "put_in_bread", # will move the bread from plate to toaster. Does nothing if toaster is already switched on.
            "take_out_bread", # will move the bread from toaster to plate. Does nothing if toaster is already switched on.
            "switch_on_toaster", # will switch the toaster on, if it is not on already.
            "wait" # will pass 10 minutes. During this time the toaster will finish toasting if it is switched on. If bread is inside it will become toasted.
        )

    # this state is only here so students can see an example. It is likely not useful.
    example_state = {
            "toaster_has_power":False, # whether or not the toaster is connected to power
            "toaster_is_on":False, # whether or not the toastere is currently on
            "bread_location":"plate", # location of the bread. This is either "plate" or "toaster"
            "bread_state":"untoasted", # state of the bread. This is either "toasted" or "untoasted"
            "time":0 # current time in minutes.
            }

    @classmethod
    def goal(cls, state):
        """
            This function defines the goal of the planning problem.
        """
        return state["bread_location"] == "plate" and state["bread_state"] == "toasted"
    
    @classmethod
    def state_transition(cls, state, action):
        """
            The state transition function. Updates the state based on which action has been chosen.
        """
        newState = state.copy()
        if action =="plug_in_toaster":
            # toaster now has power
            newState["toaster_has_power"] = True
            newState["time"] += 1
        elif action =="unplug_toaster":
            # unpower toaster and stop toasting process
            newState["toaster_has_power"] = False
            newState["toaster_is_on"] = False
            newState["time"] += 1
        elif action == "put_in_bread":
            # move bread into toaster. Only possible if toaster is not on (casue it locks)
            if not newState["toaster_is_on"]:
                newState["bread_location"] = "toaster"
            newState["time"] += 1
        elif action == "take_out_bread":
            # move bread from toaster to plate. Only possible if toaster is not on (casue it locks)
            if not newState["toaster_is_on"]:
                newState["bread_location"]="plate"
            newState["time"] += 1
        elif action == "switch_on_toaster": 
            # switch on the toaster
            if(newState["toaster_has_power"]):
                newState["toaster_is_on"]=True
            newState["time"] += 1
        elif action == "wait":
            # wait for ten steps
            newState["time"] += 10
            # if toaster is on, it is switched off, if bread was in toaster, it is toasted now.
            if newState["toaster_is_on"]:
                if newState["bread_location"] == "toaster":
                    newState["bread_state"] = "toasted"
                newState["toaster_is_on"] = False
        return newState

