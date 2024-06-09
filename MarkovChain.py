import numpy as np

class TransitionMatrix():
    def __init__(self, dim, states):
        if not dim == len(states):
            raise ValueError("Number of states must match dimension")
        
        self.dim = dim
        self.states = states
        self.transition_prob = np.zeros((dim, dim))

    def __str__(self):
        # Fix formatting
        max_elem_length = max(len(f"{x:.4f}") for x in self.transition_prob.flatten())
        max_state_length = max(len(str(state)) for state in self.states)
        elem_format = f"{{:>{max_elem_length}.4f}}"
        
        # Print states for columns
        col_indices = " " * (max_state_length + 3) + " ".join(f"{str(state):>{max_elem_length}}" for state in self.states)
        print(col_indices)
        
        # Print a separator line
        print(" " * (max_state_length + 2) + "-" * (self.dim * (max_elem_length + 1)))
        
        # Print states for rows
        for r in range(self.dim):
            row_str = f"{str(self.states[r]):>{max_state_length}} | " + " ".join(elem_format.format(self.transition_prob[r, c]) for c in range(self.dim))
            print(row_str)

        return ""

    def add_state(self, state):
        if state not in self.states:
            self.states.append(state)
            self.transition_prob = np.append(self.transition_prob, [np.zeros(self.dim)], axis=0)
            self.transition_prob = np.insert(self.transition_prob, self.dim, np.zeros(self.dim+1), axis=1)
            self.dim += 1
            return True
        else:
            return False
    
    def find_stationary_distribution(self, start_state):
        start_state_index = self.states.index(start_state)

        prev_dist = np.zeros(self.dim)
        current_dist = np.copy(prev_dist)
        current_dist[start_state_index] = 1

        # Loop until stationary distribution have been reached
        while not (current_dist==prev_dist).all():
            prev_dist = np.copy(current_dist)
            current_dist = prev_dist @ self.transition_prob

        # Find all states in stationary distribution
        end_states = dict()
        prob_winning = 0
        for i, prob in enumerate(current_dist):
            if prob != 0:
                end_states[str(self.states[i])] = round(prob, 4)
                if self.states[i][0] > 0:
                    prob_winning += prob
        
        prob_winning = round(prob_winning, 4)
        return prob_winning, end_states

    def update_transition_prob(self, from_state, to_state, prob):
        from_index = self.states.index(from_state)
        to_index = self.states.index(to_state)
        self.transition_prob[from_index, to_index] = prob
        
    def calculate_transition_prob(self, start_state):
        [a, d] = start_state

        if not self.add_state(start_state):
            return
        elif a < 0 or d < 0:
            return
        elif a == 0 and d == 0:
            return
        
        [eq_a, eq_d] = [min(a, 3), min(d, 2)]
        eq_start_state = [eq_a, eq_d]
        start_state_index = self.states.index(start_state)
        eq_start_state_index = self.states.index(eq_start_state)

        end_states = [[a-2,d], [a,d-2], [a-1,d-1], [a-1,d], [a,d-1]]
        for end_state in end_states:
            if self.add_state(end_state):
                self.calculate_transition_prob(end_state)

        if min(a, d) >= 2:
            self.transition_prob[start_state_index, self.states.index([a-2,d])] = self.transition_prob[eq_start_state_index, self.states.index([eq_a-2, eq_d])]
            self.transition_prob[start_state_index, self.states.index([a,d-2])] = self.transition_prob[eq_start_state_index, self.states.index([eq_a, eq_d-2])]
            self.transition_prob[start_state_index, self.states.index([a-1,d-1])] = self.transition_prob[eq_start_state_index, self.states.index([eq_a-1, eq_d-1])]
        elif min(a, d) == 1:
            self.transition_prob[start_state_index, self.states.index([a-1,d])] = self.transition_prob[eq_start_state_index, self.states.index([eq_a-1, eq_d])]
            self.transition_prob[start_state_index, self.states.index([a,d-1])] = self.transition_prob[eq_start_state_index, self.states.index([eq_a, eq_d-1])]
        elif min(a, d) == 0:
            self.transition_prob[start_state_index, start_state_index] = 1

def main():
    transition_matrix = TransitionMatrix(3, [[0,0], [1,0], [0,1]])
    transition_matrix.add_state([1,1])
    transition_matrix.update_transition_prob([0,0], [0,1], 0.5)
    transition_matrix.update_transition_prob([0,0], [1,0], 0.5)
    transition_matrix.update_transition_prob([1,0], [1,0], 1)
    transition_matrix.update_transition_prob([0,1], [0,1], 1)
    transition_matrix.update_transition_prob([1,1], [0,1], 0.75)
    transition_matrix.update_transition_prob([1,1], [1,0], 0.25)
    stationary_distribution = transition_matrix.find_stationary_distribution([1,1])
    print(transition_matrix)
    print(stationary_distribution)

if __name__ == "__main__":
    main()