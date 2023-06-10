from common.element import Element, fire_ele, water_ele, grass_ele, electric_ele, earth_ele, ice_ele, normal_ele

class Character:

    def __init__(self, char_id, char_name, element: Element, position, base_stats, abilities):
        """
        create an instance of a character (not a character instance)
        :param char_id: id
        :param char_name: name
        :param element: element
        :param position: position
        :param base_stats: quadruple (HP, Atk, Def, Spe)
        :param abilities: an array of Ability
        """
        self.char_id = char_id
        self.char_name = char_name
        self.element = element
        self.position = position
        self.base_stats = base_stats
        self.abilities = abilities

class Brand(Character):

    def __init__(self, level, ev=None):
        super().__init__(1, "Brand", fire_ele, "any", [70, 65, 80, 45], [])
        if ev is None:
            ev = [0, 0, 0, 0]
        self.level = level
        self.ev = ev

class Enel(Character):

    def __init__(self, level, ev=None):
        super().__init__(501, "Enel", electric_ele, "any", [105, 140, 120, 135], [])
        if ev is None:
            ev = [0, 0, 0, 0]
        self.level = level
        self.ev = ev

class Fred(Character):

    def __init__(self, level, ev=None):
        super().__init__(901, "Fred", normal_ele, "any", [130, 200, 180, 190], [])
        if ev is None:
            ev = [0, 0, 0, 0]
        self.level = level
        self.ev = ev

