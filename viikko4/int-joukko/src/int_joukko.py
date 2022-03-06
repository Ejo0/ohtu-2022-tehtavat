class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti: int  = None, kasvatuskoko: int = None):
        self.kapasiteetti = kapasiteetti if kapasiteetti else self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko else self.OLETUSKASVATUS
        self._taulukko = [None] * self.kapasiteetti
        self._alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self._taulukko

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self._taulukko[self._alkioiden_lkm] = n
        self._alkioiden_lkm += 1
        if self._alkioiden_lkm == len(self._taulukko):
            self._taulukko = self._taulukko[:]
            self._taulukko += [None] * self.kapasiteetti
            return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        
        self._taulukko.remove(n)
        self._alkioiden_lkm -= 1
        self._taulukko += [None]
        return True

    def alkioiden_maara(self):
        return self._alkioiden_lkm

    def luo_lista(self):
        return self._taulukko[:self.alkioiden_maara()]

    @staticmethod
    def yhdiste(a, b):
        output = IntJoukko()
        for n in a.luo_lista() + b.luo_lista():
            output.lisaa(n)
        return output

    @staticmethod
    def leikkaus(a, b):
        output = IntJoukko()
        for n in a.luo_lista():
            if b.kuuluu(n):
                output.lisaa(n)
        return output

    @staticmethod
    def erotus(a, b):
        output = IntJoukko()
        for n in a.luo_lista():
            if not b.kuuluu(n):
                output.lisaa(n)
        return output

    def __str__(self):
        output = ", ".join(str(n) for n in self._taulukko if n)
        return "{" + output + "}"
