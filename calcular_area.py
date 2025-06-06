
from abc import ABC, abstractmethod
import math
from typing import Protocol


class Forma(Protocol):
    @property
    def area(self) -> float:
        """Calcula a área da forma geométrica"""
        ...


class Quadrado:
    def __init__(self, lado: float):
        if lado <= 0:
            raise ValueError("Lado deve ser positivo")
        self.lado = lado

    @property
    def area(self) -> float:
        return self.lado ** 2


class Retangulo:
    def __init__(self, base: float, altura: float):
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser positivas")
        self.base = base
        self.altura = altura

    @property
    def area(self) -> float:
        return self.base * self.altura


class Circulo:
    def __init__(self, raio: float):
        if raio <= 0:
            raise ValueError("Raio deve ser positivo")
        self.raio = raio

    @property
    def area(self) -> float:
        return math.pi * (self.raio ** 2)


class FabricaFormas:
    @staticmethod
    def criar_forma(tipo: str, *args) -> Forma:
        formas = {
            'quadrado': Quadrado,
            'retangulo': Retangulo,
            'circulo': Circulo
        }

        if tipo not in formas:
            raise ValueError(f"Tipo de forma não suportado: {tipo}")

        return formas[tipo](*args)


# Exemplo de uso
if __name__ == "__main__":
    try:
        formas = [
            FabricaFormas.criar_forma('quadrado', 4),
            FabricaFormas.criar_forma('retangulo', 4, 5),
            FabricaFormas.criar_forma('circulo', 3)
        ]

        for forma in formas:
            print(f"Área: {forma.area:.2f}")

    except ValueError as e:
        print(f"Erro: {e}")
