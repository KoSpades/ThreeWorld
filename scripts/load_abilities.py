from dbservice import database_api

# Remove all tuples from Ability
database_api.remove_all_abilities()

abilities = [(1, "charge slash", 95, 3, "row", 3, 2),
             (2, "venomous blast", 125, 3, "all", 3, 4),
             ]

# Insert all abilities into Ability
for i in range(len(abilities)):
    res = database_api.create_ability(abilities[i][0],
                                      abilities[i][1],
                                      abilities[i][2],
                                      abilities[i][3],
                                      abilities[i][4],
                                      abilities[i][5],
                                      abilities[i][6],)
    if res != 0:
        print("something wrong with inserting abilities")
        break
