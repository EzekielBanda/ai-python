from FiniteStateMachine import FiniteStateMachine
"""
    The State Base Class
    The super class of 
    all the child states
"""

class State:
    # Constructor
    def __init__(self, agent):
        self.agent = agent

    def execute(self):
        pass

# Go and Sleep State Until Rested  Class
class GoHomeAndSleepStateUntilRestedState(State):
    # This state and Super Constructors
    def __init__(self, agent):
        super().__init__(agent)

    # Ruturn the reachable state for the agent
    def available_transitions(self):
        return [ "GoToWorkplaceAndMakeMoneyState"]

    def execute(self):
        # An object of the Finite State Machine
        fsm = FiniteStateMachine(self.agent, self)

        # Location of the agent
        print("\nAgent is at home and sleeping until rested.")
        print(f"Reachable States :{fsm.get_available_transitions()}")
        options = [" \n1. Not Fatigued"," \n2. Quit"]

        # Display the current State the agent is
        print(f"Current state: {type(self.agent.initial_state).__name__}\nOptions: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switching Agent from this Home to Work Place
            self.agent.initial_state = GoToWorkplaceAndMakeMoneyState(self.agent)
            
        elif choice == "2":
            print("An Agent is leaving!!!")
            # Leave the State
            exit(2) 

# Go To Bank And Deposite Money State Class
class GoToTheBankAndDepositMoneyState(State):
    # This Class Constructor
    def __init__(self, agent):
        # Super Class Constructor
        super().__init__(agent)

    # Reachable States
    def available_transitions(self):
        return ["GoToWorkplaceAndMakeMoneyState", "GoHomeAndSleepStateUntilRestedState"]

    def execute(self):
        fsm = FiniteStateMachine(self.agent, self)
        # The Location of the agent
        print("\nAgent is at the bank and depositing money.")
        # The States That Can be Transitioned
        print(f"Reachable States :{fsm.get_available_transitions()}")
        # The Transtions for the agent
        options = ["\n1. Not Satisfied With Amount In Bank","\n2. Satisfied With Amount In Bank","\n3. Quit"]

        # Display The Current State the agent is in
        print(f"Current state: {type(self.agent.initial_state).__name__}\nOptions: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switch the Agent form This State to Work Place
            self.agent.initial_state = GoToWorkplaceAndMakeMoneyState(self.agent)
        elif choice == "2":
            # Switch the Agent form This State to Home to Rest
            self.agent.initial_state = GoHomeAndSleepStateUntilRestedState(self.agent)
        elif choice == "3":
            # Quiting Action
            print("An Agent is leaving!!!")
            exit(2)

# Go to Work Place And Male Money State Class
class GoToWorkplaceAndMakeMoneyState(State):
    # Constructor
    def __init__(self, agent):
        # Super Class Constructor
        super().__init__(agent)

    # Reachable States
    def available_transitions(self):
        return ["GoToTheBankAndDepositMoneyState", "SatisfyHungerState"]

    def execute(self):
        # Finite Machine for the Agent to Work on
        fsm = FiniteStateMachine(self.agent, self)
        # The Agent Present Location
        print("\nAgent is at the workplace and making money.")
        # Reachable States from this State
        print(f"Reachable States :{fsm.get_available_transitions()}")
        # The Transition for the Agent 
        options = ["\n1. Has Made Enough Money","\n2. Is Hungry","\n3. Quit"]
        # The Present State 
        print(f"Current state: {type(self.agent.initial_state).__name__}\nOptions: {'  '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
             # Switch the Agent form This State to The Bank and Deposite Money
            self.agent.initial_state = GoToTheBankAndDepositMoneyState(self.agent)
        elif choice == "2":
             # Switch the Agent form This State to Satisfy Hunger State 
            self.agent.initial_state = SatisfyHungerState(self.agent)
        elif choice == "3":
            # Quiting Action
            print("An Agent is leaving!!!")
            exit(2)
            

# Go to Returant And Satisfy Hunger State class
class SatisfyHungerState(State):
    # This class and Super class Constructors
    def __init__(self, agent):
        super().__init__(agent)

    # Reachable State
    def available_transitions(self):
        return ["GoToWorkplaceAndMakeMoneyState"]

    def execute(self):
        # Finite Machine for the Agent to Work on
        fsm = FiniteStateMachine(self.agent, self)
        print("\nAgent is at the restaurant satisfying hunger.")
        print(f"Reachable States :{fsm.get_available_transitions()}")
        # The Transitons for the Agent
        options = ["\n1. Not Hungry","\n2. Quit"]
        # Pressent State 
        print(f"Current state: {type(self.agent.initial_state).__name__}\nOptions: {' '.join(options)}")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Switch the Agent form This State to Work place And Make Money
            self.agent.initial_state = GoToWorkplaceAndMakeMoneyState(self.agent)

        elif choice == "2":
            # Quiting the Action
            print("An Agent is leaving!!!")
            exit(2)