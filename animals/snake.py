class Snake():
    """
    A simple OOP model for snakes with basic attributes
    """
    def __init__(self, name, age, sex, poisonous):
        """
        Shows attributes of a snake
        :param name: Name given to snake
        :param age: The snake's age
        :param sex: Gender of the snake
        :param poisonous: Is the snake poisonous?
        """
        self.name = name
        self.age = age
        self.sex = sex
        self.poisonous = poisonous

    def hiss(self):
        """
        Outputs the hissing sound of the snake.
        :return: None – prints a hissing sound to the console.
        """
        print("Hisss")


