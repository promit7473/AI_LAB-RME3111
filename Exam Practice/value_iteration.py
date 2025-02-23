# Question 1: Implement the **Value Iteration** algorithm to compute the value function
# for the following environment where:
# - States: S0, S1, S2
# - Actions: A0, A1
# - Transitions:
#   * S0 -> A0 -> (S1, Reward: 1), (S2, Reward: 2)
#   * S1 -> A0 -> (S2, Reward: 3)
#   * S2 -> A1 -> (S0, Reward: 1)
# - Gamma = 0.9 (discount factor), Theta = 1e-6 (stopping criterion)

def value_iteration(env, gamma=0.9, theta=1e-6):
    # Initialize value function to 0 for all states
    V = {state: 0 for state in env.get_all_states()}
    while True:
        delta = 0
        # Iterate through all states
        for state in env.get_all_states():
            v = V[state]
            # Update value of state by taking the maximum over all actions
            V[state] = max(
                sum(1 * (reward + gamma * V[next_state]) for next_state, reward in env.get_transitions(state, action))
                for action in env.get_possible_actions(state)
            )
            delta = max(delta, abs(v - V[state]))
        # Stop if the change is smaller than the threshold (theta)
        if delta < theta:
            break
    return V

# Answer for Question 1:
# The output of the value iteration will give the optimal value function for each state.
# The computed value function reflects the long-term reward for each state.

# Question 2: Implement the **Policy Evaluation** algorithm to compute the value function
# for a given policy where:
# - Policy: {'S0': 'A0', 'S1': 'A0', 'S2': 'A0'}
# - Same environment as Question 1
# - Gamma = 0.9, Theta = 1e-6

def policy_evaluation(policy, env, gamma=0.9, theta=1e-6):
    # Initialize value function to 0 for all states
    V = {state: 0 for state in env.get_all_states()}
    while True:
        delta = 0
        # Iterate through all states
        for state in env.get_all_states():
            v = V[state]
            # Get the action from the policy
            action = policy[state]
            # Update value of state based on policy's action
            V[state] = sum(1 * (reward + gamma * V[next_state]) for next_state, reward in env.get_transitions(state, action))
            delta = max(delta, abs(v - V[state]))
        # Stop if the change is smaller than the threshold (theta)
        if delta < theta:
            break
    return V

# Answer for Question 2:
# The output of the policy evaluation will give the value function based on the given policy.
# It tells us the expected long-term rewards starting from each state under the given policy.

# Mock Environment for testing the above algorithms
class MockEnvironment:
    def __init__(self):
        # Define states, actions, and transitions
        self.states = ['S0', 'S1', 'S2']
        self.transitions = {
            'S0': [('A0', 'S1', 1), ('A0', 'S2', 2)],
            'S1': [('A0', 'S2', 3)],
            'S2': [('A1', 'S0', 1)],
        }
        self.actions = {
            'S0': ['A0'],
            'S1': ['A0'],
            'S2': ['A1'],
        }

    def get_all_states(self):
        return self.states

    def get_transitions(self, state, action):
        # Return the transitions for a given state and action
        return [(next_state, reward) for action_, next_state, reward in self.transitions.get(state, []) if action_ == action]

    def get_possible_actions(self, state):
        return self.actions.get(state, [])


# Example usage:

# Initialize environment
env = MockEnvironment()

# Example of Value Iteration
print("Value Iteration Result:")
V = value_iteration(env)
print(V)

# Example of Policy Evaluation
# Assume an initial policy where the policy always selects action 'A0' for all states
policy = {'S0': 'A0', 'S1': 'A0', 'S2': 'A0'}

print("\nPolicy Evaluation Result:")
V_policy = policy_evaluation(policy, env)
print(V_policy)

