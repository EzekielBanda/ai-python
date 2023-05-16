
"""
    The class that houses everthing that an agent
    needs 
"""
class FiniteStateMachine:
    # Constructor with Agent And State
    def __init__(self, agent, state):
        self.agent = agent
        self.state = state

    # Instruct Agent to Start Working
    def execute(self):
        self.agent.initial_state.execute()

    # Avalibale State in the Machine
    def get_available_transitions(self):
        return self.agent.initial_state.available_transitions() 