from kps import KPS
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly

class KPSBuilder:
    def __init__(self, peli = KPS()):
        self._peli = peli

    def pelaa(self):
        self._peli.pelaa()

    def kps_parempi_tekoaly(self):
        return KPSBuilder(KPSParempiTekoaly())
    
    def kps_tekoaly(self):
        return KPSBuilder(KPSTekoaly())
    
    def kps_pelaaja_vs_pelaaja(self):
        return KPSBuilder(KPSPelaajaVsPelaaja())
