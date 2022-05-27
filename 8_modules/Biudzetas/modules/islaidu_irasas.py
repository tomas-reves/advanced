from .irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, isigyta_preke_paslauga, atsiskaitymo_budas):
        super().__init__(suma)
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
        self.atsiskaitymo_budas = atsiskaitymo_budas