from utils import util

fire_starter_base = [70, 65, 75, 45]
fred_base = [120, 190, 170, 180]

fire_starter_stats = util.calc_actual_stats(fire_starter_base, [0, 0, 0, 0], 5)
fred_stats = util.calc_actual_stats(fred_base, [100, 100, 100, 100], 50)
util.print_status(fire_starter_stats, "fire starter")
util.print_status(fred_stats, "Fred")
print(f"Your dmg is {util.calc_dmg(5, 40, fire_starter_stats[1], fred_stats[2], 1, 1)}")
print(f"Fred dmg is {util.calc_dmg(50, 120, fred_stats[1], fire_starter_stats[1], 1, 1)}")
