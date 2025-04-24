class Cat():
    """
    This is the class Cat that implements a cat with 3 attributes (name, nickname, cry and locations)
    """
    def __init__(self):
        self.name = "Pat"
        self.nickname = "FatPat"
        self.cry = "Meow"
        self.locations = []

    def speak(self):
        """
        Causes the cat to make its signature cry.
        :return: None – prints the cry sound to the console.
        """
        print(self.cry)

    def explore(self, location):
        """
        Method to take a location and add it to the list of locations.
        :param location: String which represents the location that the cat explores
        :return: None – prints message to the console.
        """

        print(f"{self.nickname} is exploring the {location}")
        self.locations.append(location)

pat = Cat()
pat.speak()
pat.explore("Bed Room")


