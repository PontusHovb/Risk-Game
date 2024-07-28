import ast
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import Modules.SimulatedAttack as SimulatedAttack
import Modules.MarkovChain as MarkovChain

DIM = 31*31-1
STATES = 'states.txt'
TRANSITION_MATRIX = 'transition_matrix.npy'

def plot_simulation(no_attackers, no_defenders, NSIM=5000, NO_UPDATES=50, update_delay=500):
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Monte Carlo Simulation
    remaining_attackers = np.zeros(no_attackers+1)
    bars = ax.bar(range(no_attackers+1), remaining_attackers, color='blue', width=0.4, label='Monte Carlo Simulation')
    simulation_count = [0]

    # Theorical values (Markov Chain)
    theoretical_values = calculate_theoretical(no_attackers, no_defenders)
    theoretical_line, = ax.plot(range(no_attackers+1), theoretical_values, color='red', linestyle='--', label='Markov Chain')

    # Prepare plot
    ax.legend()
    ax.set_ylim(0, 0.15)
    
    def update(frame):
        for _ in range(NSIM//NO_UPDATES):
            remaining_attackers[SimulatedAttack.simulated_attack(no_attackers, no_defenders)[0]] += 1
            simulation_count[0] += 1
        
        for bar, new_height in zip(bars, remaining_attackers / simulation_count[0]):
            bar.set_height(new_height)

        ax.set_xlabel("Remaining attackers")
        ax.set_ylabel("Probability")
        ax.set_title(f"Simulation {simulation_count[0]} of {NSIM}")

    # Create animation with pause and update delay
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=(NO_UPDATES)-1, 
        repeat=False, 
        interval=100
    )

    # Show plot
    time.sleep(1)
    plt.show()

def calculate_theoretical(no_attackers, no_defenders):
    # Read transition matrix
    with open(TRANSITION_MATRIX, 'rb') as f:
        transition_matrix_file = np.load(f, allow_pickle=True)

    # Read states
    states = []
    with open(STATES, 'r') as f:
        for line in f:
            states.append(ast.literal_eval(line.strip()))
    
    # Create transition matrix object
    transition_matrix = MarkovChain.TransitionMatrix(DIM, states, transition_matrix_file)
    prob_winning, end_states = transition_matrix.find_stationary_distribution([no_attackers, no_defenders])

    # Calculate remaining attackers
    remaining_attackers = np.zeros(no_attackers+1)
    for end_state_str, prob in end_states.items():
        end_state = ast.literal_eval(end_state_str)
        remaining_attackers[end_state[0]] += prob
        
    return remaining_attackers

def main():
    plot_simulation(20, 10, NO_UPDATES = 100)

if __name__ == '__main__':
    main()
