from dbservice import database_api

# Remove all tuples from Character
database_api.remove_all_characters()

abilities = [(906, "Nemesis", 3, "any", 125, 125, 125, 125),
             ]

# Insert all abilities into Ability
for i in range(len(abilities)):
    res = database_api.create_character(abilities[i][0],
                                        abilities[i][1],
                                        abilities[i][2],
                                        abilities[i][3],
                                        abilities[i][4],
                                        abilities[i][5],
                                        abilities[i][6],
                                        abilities[i][7], )
    if res != 0:
        print("something wrong with inserting characters")
        break
