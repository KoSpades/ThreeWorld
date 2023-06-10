from utils import util
from common.character import *

# We need to move all the numbers into a database!!!
# Starting from element

lucy_brand = Brand(5)
lucy_enel = Enel(60)
npc_fred = Fred(60)


lucy_brand_stats = util.calc_actual_stats(lucy_brand)
lucy_enel_stats = util.calc_actual_stats(lucy_enel)
npc_fred_stats = util.calc_actual_stats(npc_fred)
util.print_status(lucy_brand_stats, "Lucy's brand")
util.print_status(lucy_enel_stats, "Lucy's enel")
util.print_status(npc_fred_stats, "NPC Fred")
print(f"Enel dmg is {util.calc_dmg(60, 90, lucy_enel_stats[1], npc_fred_stats[2], 1, 1)}")
print(f"Fred dmg is {util.calc_dmg(60, 150, npc_fred_stats[1], lucy_enel_stats[2], 1, 1)}")

