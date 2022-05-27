class PersonalCode:
    def __init__(self, kodas):
        self.kodas = kodas

    def return_last_4(self):
        return self.kodas[-3:]