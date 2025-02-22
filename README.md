# Risk Game
<p align="center">
    <img src="https://github.com/PontusHovb/Risk-Game/blob/master/Images/RiskGame.jpeg" width="400"/>
</p>
Risk is a board game where the goal is to use your troops to capture territories and eliminate other players. Territories are captured in a battle when an attacker chooses to invade a territory of another player. The battle is simulated with dice roles where the attacker can attack with a maximum of 3 dices and the defender can have a maximum of 2 dices to defend themselves. In a battle the highest rolled dices are matched and the rest are discarded. If the attacker have troops left after an "attack" (dice roll) they can choose to attack again until the territory is captured (defender has no troops left) or the attacker has no more available troops.

A single "attack" (dice roll) can have a maximum of 3 attackers and 2 defender. Therefore, if either player has more troops to their disposal the rest of the troops can't participate in the "attack" but can of course be saved to future "attacks"

# Markov Chain
<p align="center">
    <img src="https://github.com/PontusHovb/Risk-Game/blob/master/Images/MarkovChain_30troops.png" width="400"/>
</p>
<p align="center"><i>Probability of winning for up to 30 attackers and defenders</i></p>
The theoretical probability of winning can be computed using a Markov Chain. The states are unique combinations of attackers and defenders, denoted as $(a,d)$, with $a$ as number of attackers and $d$ as number of defenders. The transition matrix can then be created and the theoretical probability of winning is the stationary distribution from the respective start state. The theoretical probability of winning with $0 \ge a \le 10$ attackers and $0 \ge d \le 10$ defenders are illustrated with the heatmap to the left. This method is beneficial when calculating probabilty for many different states since transition probabilities only needs to be calculated once. However, for estimating the winning probability from a single state this method is not as fast since all transition probabilities for all possible states have to be calculated.
<p align="center">
    <img src="https://github.com/PontusHovb/Risk-Game/blob/master/Images/MarkovChain_10troops.png" width="400"/>
</p>
<p align="center"><i>Probability of winning for up to 10 attackers and defenders</i></p>

# Monte Carlo simulations
<p align="center">
    <img src="https://github.com/PontusHovb/Risk-Game/blob/master/Images/MCS.gif" width="400"/>
</p>
<p align="center"><i>Simulation of Monte Carlo compared to theoretical probabilities from Markov Chain</i></p>
Another method to estimate the probability of winning is through Monte Carlo Simulations. With this method a large number of attacks are simulated whereafter the probability distribution is estimated. As seen on the heatmap to the left, the estimated probabilties are close to theoratical probabilities using 20.000 simulations per uunique combination of no. attackers and no. defender $(a,d)$. This method is preferred when estimating the winning probability for a large number of troops when we are interested in only a single combination. However, when calculating probabilities for many different combinations (to e.g. create this heatmap) Monte Carlo simulations are slow since 20.000 simulations need to be performed for every single combination and we can't use previous estimated probabilities.
