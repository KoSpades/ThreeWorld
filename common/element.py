class Element:

    def __init__(self, element_id):
        """
        create an instance of an element
        :param element_id: id
        :param element_name: name
        :param strength: which elements this element is strong against
        :param weakness: which elements this element is weak against
        """
        self.element_id = element_id
        if self.element_id == 1:
            self.name = "fire"
            self.strength = [2, 6]
            self.weakness = [3, 5]
        elif self.element_id == 2:
            self.name = "grass"
            self.strength = [3, 5]
            self.weakness = [1, 6]
        elif self.element_id == 3:
            self.name = "water"
            self.strength = [1, 5]
            self.weakness = [2, 4]
        elif self.element_id == 4:
            self.name = "electric"
            self.strength = [3]
            self.weakness = [5]
        elif self.element_id == 5:
            self.name = "earth"
            self.strength = [1, 4]
            self.weakness = [2, 3]
        elif self.element_id == 6:
            self.name = "ice"
            self.strength = [2]
            self.weakness = [1]
        elif self.element_id == 7:
            self.name = "normal"
            self.strength = []
            self.weakness = []
        else:
            print("Type Not Implemented")


fire_ele = Element(1)
grass_ele = Element(2)
water_ele = Element(3)
electric_ele = Element(4)
earth_ele = Element(5)
ice_ele = Element(6)
normal_ele = Element(7)
