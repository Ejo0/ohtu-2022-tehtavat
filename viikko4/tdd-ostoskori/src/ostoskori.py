from functools import reduce
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostoslista = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.ostokset())

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.ostokset())

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostoslista:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        self._ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._ostoslista:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
                break
        if ostos.lukumaara() == 0:
            self._ostoslista.remove(ostos)

    def tyhjenna(self):
        self._ostoslista.clear()

    def ostokset(self):
        return self._ostoslista
