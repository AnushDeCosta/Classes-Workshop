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
        Simulates the snake coiling up its body.
        :return: None - prints a message with the snake's name to the console.
        """
        sound = '"Hisssss"'
        print(f"{sound}")

    def coil(self):
        """
        Simulates the snake coiling up it's body
        :return: None - prints a message to the console
        """
        print(f"{self.name} coils up its own body")

snake = Snake("Squinky", 2, "Male", False)

snake.hiss()
snake.coil()

