from dbservice import database_api

# Remove all tuples from Character and Ability
database_api.remove_all_characters()
database_api.remove_all_abilities()

# Insert all characters into Character

characters = [(906, "Nemesis", 3, "any", 125, 125, 125, 125),
              ]

for i in range(len(characters)):
    res = database_api.create_character(characters[i][0],
                                        characters[i][1],
                                        characters[i][2],
                                        characters[i][3],
                                        characters[i][4],
                                        characters[i][5],
                                        characters[i][6],
                                        characters[i][7],
                                        )
    if res != 0:
        print("something wrong with inserting characters")
        break

# Insert all abilities into Ability

abilities = [(1, "charge slash", 906, 95, 3, "row", 3, 2),
             (2, "venomous blast", 906, 125, 3, "all", 3, 4),
             ]

for i in range(len(abilities)):
    res = database_api.create_ability(abilities[i][0],
                                      abilities[i][1],
                                      abilities[i][2],
                                      abilities[i][3],
                                      abilities[i][4],
                                      abilities[i][5],
                                      abilities[i][6],
                                      abilities[i][7], )
    if res != 0:
        print("something wrong with inserting abilities")
        break
