class Carta:
    def __init__(self,pinta:str,valor:str):
        self.pinta:str = pinta
        self.valor: str = valor
        self.tapada: bool = true

class Mano:
    def __init__(self, cartas: list[Carta]):
        self.cartas: list[Carta] = []
        self,cartas.extend(cartas)

    def es_blackjack(self) -> bool:
        pass
class baraja:
    PINTAS: list[str] = ["\u2764\uFE0F","\u2660\uFE0F","\u2666\uFE0F","\u2663\uFE0F"]
    VALORES: list[str] = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __init__(self):
        self.cartas: list[Carta] = []
        for pinta in baraja.PINTAS:
            for valor in baraja.VALORES:
                self.cartas.append(carta(pinta.valor))

    def revolver(self):
        pass

    def repartir_carta(self,tapada = False ) -> Carta:
        pass

    def repartir_carta_adicional(self):
        pass

class Jugador:
    def __init__(self, nombre: str, fichas: int):
        self.nobre:str = nombre
        self.fichas:int = fichas
        self.mano: Mano = None

    def inicializar_mano(self,cartas: list[Carta]):
        self.mano = Mano(cartas)

    def seleccionar_jugada(self):
        pass

    def pedir_carta(self):
        pass

    def plantarse(self):
        pass

class Blackjack:
    def __init__(self):
        sel.apuesta_inicial: int = 0
        self.jugador: jugador = None
        self.cupier: Casa = None
        self.baraja: Baraja = Baraja()

    def registrar_usuario(self,nombre: str):
        pass

    def iniciar_juego(self,apuesta: int):
        pass

    def destapar_carta_casa(self):
        pass

    def hacer_jugada_casa(self):
        pass

    def evaluar_mano_casa(self):
        pass

    def repartir_mano_casa(self):
        pass

    def comparar_manos(self):
        pass

    def finalizar_juego(self):
        pass



