from .islaidu_irasas import IslaiduIrasas
from .pajamu_irasas import PajamuIrasas
from .irasas import Irasas

class Biudzetas(Irasas):
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, isigyta_preke_paslauga, atsiskaitymo_budas):
        islaidos = IslaiduIrasas(suma, isigyta_preke_paslauga, atsiskaitymo_budas)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas,PajamuIrasas):
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                suma += irasas.suma
        return f"{suma} EUR"

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos {irasas.suma} $, siuntejas: {irasas.siuntejas}, papildoma info: {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Islaidos: {irasas.suma} $, preke ar paslauga: {irasas.isigyta_preke_paslauga}, atsiskaitymo budas:{irasas.atsiskaitymo_budas}")
