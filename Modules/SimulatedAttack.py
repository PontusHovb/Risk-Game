import random

def simulated_attack(no_attackers, no_defenders):
    a1 = random.randint(1,6)
    a2 = random.randint(1,6)
    a3 = random.randint(1,6)
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if no_attackers >= 3 and no_defenders >= 2:
        if sorted([a1,a2,a3])[-1] > sorted([d1,d2])[-1]:
            if sorted([a1,a2,a3])[-2] > sorted([d1,d2])[-2]:
                return simulated_attack(no_attackers, no_defenders-2)
            else:
                return simulated_attack(no_attackers-1, no_defenders-1)
        else:
            if sorted([a1,a2,a3])[-2] > sorted([d1,d2])[-2]:
                return simulated_attack(no_attackers-1, no_defenders-1)
            else:
                return simulated_attack(no_attackers-2, no_defenders)
    elif no_attackers >= 3 and no_defenders == 1:
        if max(a1,a2,a3) > d1:
            return [no_attackers, 0]
        else:
            return simulated_attack(no_attackers-1, no_defenders)
    elif no_attackers == 2 and no_defenders >= 2:
        if sorted([a1,a2])[-1] > sorted([d1,d2])[-1]:
            if sorted([a1,a2])[-2] > sorted([d1,d2])[-2]:
                return simulated_attack(no_attackers, no_defenders-2)
            else:
                return simulated_attack(no_attackers-1, no_defenders-1)
        else:
            if sorted([a1,a2])[-2] > sorted([d1,d2])[-2]:
                return simulated_attack(no_attackers-1, no_defenders-1)
            else:
                return [0, no_defenders]
    elif no_attackers == 2 and no_defenders == 1:
        if max(a1, a2) > d1:
            return [no_attackers, 0]
        else:
            return simulated_attack(1, 1)
    elif no_attackers == 1 and no_defenders >= 2:
        if a1 > max(d1, d2):
            return simulated_attack(1, no_defenders-1)
        else:
            return [0, no_defenders]
    elif no_attackers == 1 and no_defenders == 1:
        if a1 > d1:
            return [1, 0]
        else:
            return [0, 1]
    elif no_attackers == 0:
        return [0, no_defenders]
    elif no_defenders == 0:
        return [no_attackers, 0]

if __name__ == '__main__':
    nsim = 100
    wins = 0

    for n in range(0, nsim):
        if(simulated_attack(4,4) == 'W'):
            wins += 1

    print("Probability of attacker winning {:.1%}".format(wins/nsim))
