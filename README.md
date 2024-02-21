In the board game Risk an attack is simulated by throwing dices. 

The attacker can choose to attack with a maximum of 3 troops, and the defender defending with a maximum of 2 troops.
The highest dice of the attacker is compared to the highest of the defender.
In the case that both players have at least two dices the second highest of the attacker is compared to the second highest of the defender.
For each pair, if the attacker's dice is higher, the defender looses one troop. If the dices are equal or the defender has the highest dice, the attacker looses one troop.

In this project, several mathematical concepts are used to model and gain insights in how an attack would play out.
* **Theoretical Probabilities.ipynb** For individual attacks (max 3 attackers & 2 defenders) it is possible to calculate the theoretical probabilities using casework counting
* **Monte Carlo Simultions.ipynb** For large number of troops it is not possible to count all possible cases. Instead Monte Carlo Simulations are used to estimate probabilities
