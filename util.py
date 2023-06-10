import numpy as np
import random

fire_starter_base = [70, 65, 75, 45]
fred_base = [120, 190, 170, 180]

def calc_actual_stats(base_stat, ev, level):
    """
    calculate actual stats based on base stats
    :param base_stat: quadruple (HP, atk, def, spe) with the base stats
    :param ev: quadruple with the effort value, max total is 400
    :param level: level of hero
    :return: quadruple with the actual stats
    """
    return np.round((2*np.array(base_stat)+np.array(ev)/4)*level/60 + np.array([5, 5, 5, 5])).astype(int)

def calc_dmg(level, power, attack, defense, type_mod, crit_mod):
    """
    calculate damage dealt by an attacker to a defender
    :param level: attacker lv
    :param power: ability power
    :param attack: attack atk
    :param defense: defender def
    :param type_mod: type modifier (2, 0,5, 1, or 0)
    :param crit_mod: (2 or 1)
    :return: damage dealt, integer
    """
    rand_mod = random.randint(217, 255)
    return round(((((((2 * level) / 5) + 2) * power * (attack / defense)) / 50) + 2)
                 * type_mod * crit_mod * rand_mod/255)

def print_status(stats, name):
    """
    Given a hero's actual stats and name, print out the stats
    :param stats: an array of actual stats
    :param name: name of the hero
    :return: None
    """
    print(f"{name}'s stats is:")
    print(f"HP: {stats[0]}")
    print(f"Atk: {stats[1]}")
    print(f"Def: {stats[2]}")
    print(f"Spe: {stats[3]}")


fire_starter_stats = calc_actual_stats(fire_starter_base, [0, 0, 0, 0], 5)
fred_stats = calc_actual_stats(fred_base, [100, 100, 100, 100], 50)
print_status(fire_starter_stats, "fire starter")
print_status(fred_stats, "Fred")
print(f"Your dmg is {calc_dmg(5, 40, fire_starter_stats[1], fred_stats[2], 1, 1)}")
print(f"Fred dmg is {calc_dmg(50, 120, fred_stats[1], fire_starter_stats[1], 1, 1)}")

