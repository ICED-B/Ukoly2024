from __future__ import annotations  #test4
from typing import Union
import random
class Matice:
    def __init__(self, n: int, m: int, data=None):
        """Inicializuje matici n x m."""
        self.n = n
        self.m = m
        if data:
            self.data = data
        else:
            self.data = []
            for i in range(n):
                radek = []
                for j in range(m):
                    radek.append(random.randint(0, 9))
                self.data.append(radek)
    def __str__(self) -> str:
        """Vrátí stringovou reprezentaci matice."""
        return "\n".join(" ".join(map(str, radek)) for radek in self.data)
    def __eq__(self, other: object) -> bool:  
        """Porovná aktuální matici s maticí other."""
        if not isinstance(other, Matice):  
            return False # vrátí False
        return self.n == other.n and self.m == other.m and self.data == other.data  
    def __add__(self, other: Matice) -> Matice:
        """Sečte aktuální matici s maticí other."""
        if len(self.data) == len(other.data) and all(len(row) == len(other.data[i]) for i, row in enumerate(self.data)): # kontrola rozměrů matic
            matice = []
            for i in range(len(self.data)):
                radek = []
                for j in range(len(self.data[i])):
                    radek.append(self.data[i][j] + other.data[i][j]) 
                matice.append(radek)
            return Matice(len(self.data), len(self.data[0]), matice)
        else:
            raise ValueError("Matice nemají stejné rozměry")
    def __mul__(self, other: Union[Matice, int]) -> Union[Matice, int]:
        """Vynásobí aktuální matici maticí nebo skalárem."""
        if isinstance(other, Matice):  
            if len(self.data[0]) == len(other.data):  
                matice = []
                for i in range(len(self.data)):
                    radek = []
                    for j in range(len(other.data[0])):
                        hodnota = 0
                        for k in range(len(self.data[0])):
                            hodnota += self.data[i][k] * other.data[k][j]
                        radek.append(hodnota)
                    matice.append(radek)
                return Matice(len(self.data), len(other.data[0]), matice)
            else:
                raise ValueError("Matice nejsou kompatibilní pro násobení")
        elif isinstance(other, int):
            matice = []
            for i in range(len(self.data)):
                radek = []
                for j in range(len(self.data[i])):
                    radek.append(self.data[i][j] * other)
                matice.append(radek)
            return Matice(len(self.data), len(self.data[0]), matice)
    def transpozice(self) -> Matice:
        """Vrátí transponovanou matici."""
        if not self.data or not self.data[0]:
            return Matice(0, 0, [])
        matice = []
        for i in range(len(self.data[0])):
            radek = []
            for j in range(len(self.data)):
                radek.append(self.data[j][i])
            matice.append(radek)
        return Matice(len(self.data[0]), len(self.data), matice)
if __name__ == "__main__":
    matice1 = Matice(3, 2)
    matice2 = Matice(2, 4)

    print("Matice 1:")
    print(matice1)
    print("Matice 2:")
    print(matice2)

    soucet = matice1+matice1  
    print("Součet matic:")
    print(soucet)

    nasobek = matice1*matice2  
    print("Násobení matic:")
    print(nasobek)

    skalarni_nasobek = matice1*10
    print("Skálární násobek:")
    print(skalarni_nasobek)

    transponovana = matice1.transpozice()
    print("Transponovaná matice:")
    print(transponovana)

