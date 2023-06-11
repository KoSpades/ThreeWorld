class Ability:

    def __init__(self, a_id, a_name, power, element, target_type):
        """
        :param target_type: single, row, column, or all
        """
        self.a_id = a_id
        self.a_name = a_name
        self.power = power
        self.element = element
        self.target_type = target_type

