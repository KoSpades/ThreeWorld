from dbservice import database_api

# Remove all tuples from Element and ElementRelation
database_api.remove_all_element_relations()
database_api.remove_all_elements()

elements = [(1, "fire"), (2, "water"), (3, "grass"), (4, "electric"),
            (5, "earth"), (6, "ice"), (7, "normal"), (8, "dragon"),
            (9, "soul"), (10, "light"), (11, "spacetime")]

# Insert all elements into Element
for i in range(len(elements)):
    res = database_api.create_element(elements[i][0], elements[i][1])
    if res != 0:
        print("something wrong with inserting elements")
        break

element_relations = [(1, 1, 1), (1, 2, 0.5), (1, 3, 2), (1, 4, 1), (1, 5, 0.5), (1, 6, 2),
                     (1, 7, 1), (1, 8, 0.5), (1, 9, 1), (1, 10, 1), (1, 11, 1),
                     (2, 1, 2), (2, 2, 1), (2, 3, 0.5), (2, 4, 0.5), (2, 5, 2), (2, 6, 1),
                     (2, 7, 1), (2, 8, 0.5), (2, 9, 1), (2, 10, 1), (2, 11, 1),
                     (3, 1, 0.5), (3, 2, 2), (3, 3, 1), (3, 4, 1), (3, 5, 2), (3, 6, 0.5),
                     (3, 7, 1), (3, 8, 0.5), (3, 9, 1), (3, 10, 1), (3, 11, 1),
                     (4, 1, 1), (4, 2, 2), (4, 3, 1), (4, 4, 1), (4, 5, 0.5), (4, 6, 1),
                     (4, 7, 1), (4, 8, 0.5), (4, 9, 1), (4, 10, 1), (4, 11, 1),
                     (5, 1, 2), (5, 2, 0.5), (5, 3, 0.5), (5, 4, 2), (5, 5, 1), (5, 6, 1),
                     (5, 7, 1), (5, 8, 0.5), (5, 9, 1), (5, 10, 1), (5, 11, 1),
                     (6, 1, 0.5), (6, 2, 1), (6, 3, 2), (6, 4, 1), (6, 5, 1), (6, 6, 1),
                     (6, 7, 1), (6, 8, 0.5), (6, 9, 1), (6, 10, 1), (6, 11, 1),
                     (7, 1, 1), (7, 2, 1), (7, 3, 1), (7, 4, 1), (7, 5, 1), (7, 6, 1),
                     (7, 7, 1), (7, 8, 1), (7, 9, 0), (7, 10, 1), (7, 11, 1),
                     (8, 1, 1), (8, 2, 1), (8, 3, 1), (8, 4, 1), (8, 5, 1), (8, 6, 1),
                     (8, 7, 1), (8, 8, 1), (8, 9, 1), (8, 10, 1), (8, 11, 1),
                     (9, 1, 1), (9, 2, 1), (9, 3, 1), (9, 4, 1), (9, 5, 1), (9, 6, 1),
                     (9, 7, 2), (9, 8, 1), (9, 9, 2), (9, 10, 1), (9, 11, 1),
                     (10, 1, 2), (10, 2, 2), (10, 3, 2), (10, 4, 2), (10, 5, 2), (10, 6, 2),
                     (10, 7, 1), (10, 8, 1), (10, 9, 1), (10, 10, 1), (10, 11, 1),
                     (11, 1, 1), (11, 2, 1), (11, 3, 1), (11, 4, 1), (11, 5, 1), (11, 6, 1),
                     (11, 7, 1), (11, 8, 2), (11, 9, 2), (11, 10, 2), (11, 11, 2),
                     ]

# Insert all element relations into ElementRelation
for i in range(len(element_relations)):
    res = database_api.create_element_relation(element_relations[i][0],
                                               element_relations[i][1],
                                               element_relations[i][2],)
    if res != 0:
        print("something wrong with inserting element relations")
        break


