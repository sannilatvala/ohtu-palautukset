KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("kapasiteetti2")

        self._kapasiteetti = kapasiteetti
        self._kasvatuskoko = kasvatuskoko

        self._lista = self._luo_lista(self._kapasiteetti)

        self._alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        if n in self._lista[:self._alkioiden_lkm]:
            return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self._lista[self._alkioiden_lkm] = n
            self._alkioiden_lkm += 1

            if self._alkioiden_lkm == len(self._lista):
                self._kasvata_lista()
            return True
        return False

    def _kasvata_lista(self):
        uusi_lista = self._luo_lista(self._alkioiden_lkm + self._kasvatuskoko)
        self.kopioi_lista(self._lista, uusi_lista)
        self._lista = uusi_lista

    def kopioi_lista(self, lahde_lista, kohde_lista):
        kohde_lista[:len(lahde_lista)] = lahde_lista

    def poista(self, n):
        if n in self._lista[:self._alkioiden_lkm]:
            self._lista.remove(n)
            self._alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self._alkioiden_lkm

    def to_int_list(self):
        return self._lista[:self._alkioiden_lkm]

    @staticmethod
    def yhdiste(lista1, lista2):
        joukko_x = IntJoukko()
        for luku in lista1.to_int_list() + lista2.to_int_list():
            joukko_x.lisaa(luku)
        return joukko_x

    @staticmethod
    def leikkaus(lista1, lista2):
        joukko_y = IntJoukko()

        for luku in lista1.to_int_list():
            if lista2.kuuluu(luku):
                joukko_y.lisaa(luku)

        return joukko_y

    @staticmethod
    def erotus(lista1, lista2):
        joukko_z = IntJoukko()

        for luku in lista1.to_int_list():
            if not lista2.kuuluu(luku):
                joukko_z.lisaa(luku)

        return joukko_z

    def __str__(self):
        return "{" + ", ".join(map(str, self._lista[:self._alkioiden_lkm])) + "}"
