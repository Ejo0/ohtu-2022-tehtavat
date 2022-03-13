# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        self._muisti.append(siirto)
        if len(self._muisti) > self._muistin_koko:
            self._muisti.pop(0)

    def anna_siirto(self):
        if len(self._muisti) < 2:
            return "k"

        vastaustajan_viimeisin = self._muisti[-1]

        k = 0
        p = 0
        s = 0

        for i in range(0, len(self._muisti) - 2):
            if vastaustajan_viimeisin == self._muisti[i]:
                vastustajan_seuraava = self._muisti[i + 1]

                if vastustajan_seuraava == "k":
                    k += 1
                elif vastustajan_seuraava == "p":
                    p += 1
                else:
                    s += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        if k > p and k > s:
            return "p"
        elif p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
