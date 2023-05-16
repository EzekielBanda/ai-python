from Agent import Agent
from FiniteStateMachine import FiniteStateMachine

"""
    The main,
    Whenever you want run this project
    Run this class
"""
if __name__ == "__main__":
    agent = Agent()
    # 
    fsm = FiniteStateMachine(agent, agent.initial_state)

    # Let agent to Move Around the Machine state
    while True:
        fsm.agent.initial_state.execute()