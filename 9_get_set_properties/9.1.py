"""Sukurkite klasę “Player”:
1. Ji turi turėti atributą name, lives (su property ir setter) (reikšmę priskirti ir inicializuojant objektą)
2. Metodą hit, kurį panaudojus žaidėjo gyvybės mažėja
3. Read-only property is_alive, kuris, nebelikus gyvybių, gražintų False

"""

class Player:
    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, new_lives):
        self._lives = new_lives

    @property
    def is_alive(self):
        if self.lives > 0:
            return True

p = Player("Tomas", 2)

while p.is_alive:
    print(f"{p.name} has {p.lives} lives")
    hit = int(input("Enter 1 to reduce number of live by 1"))
    if hit == 1:
        p.hit()
    else:
        print("wrong number entered")

print(f"{p.name} has no more lives left")