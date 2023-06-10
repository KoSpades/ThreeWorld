class Grid:

    def __init__(self, char_instance_id=None):
        """
        for initializing a grid
        :param char_instance_id: the id of a character instance that currently occupies the grid
                0 if none exists
        """
        self.char_instance_id = char_instance_id

