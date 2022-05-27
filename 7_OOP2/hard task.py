"""# Kiekvienas Teletabis turi spalvą
# Pou turi paspirtuka


teletubies = TeletubyShow(TinkiWinki(), Dipsi(), LaLa(), Pou())
[teletubie for teletubie in teletubies]
# Turetu isspausdinti:
# TinkiWinki is purple
# Dipsi is green
# Lala is yellow
# Pou is red and rides a scooter
"""

class TeletubyShow():
    def __init__(self, *args):
        self.teletuby_characters = []
        for ch in args:
            self.teletuby_characters.append(ch)

    def __iter__(self):
    #     for character in self.teletuby_characters:
    #         print(f"{character.__class__.__name__} is {chacater.color}")
        return iter(self.teletuby_characters)

class TinkiWinki:
    def __init__(self, color='purple'):
        self.color = color

    def __str__(self):
        return f"Tinki Winki is {self.color}"

class Dipsi:
    def __init__(self, color='green'):
        self.color = color

    def __str__(self):
        return f"Dipsi is {self.color}"

class Lala:
    def __init__(self, color='yellow'):
        self.color = color

    def __str__(self):
        return f"Lala is {self.color}"

class Pau:
    def __init__(self, rides='scooter', color='yellow'):
        self.color = color
        self.rides = rides

    def __str__(self):
        return f"Pau is {self.color} and rides {self.rides}"

teletubies = TeletubyShow(TinkiWinki(), Dipsi(), Lala(), Pau())

[teletubie for teletubie in teletubies]